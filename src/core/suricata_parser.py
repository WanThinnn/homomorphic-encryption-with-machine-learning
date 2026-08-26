"""
Suricata Log Parser for UNSW-NB15 ML Model
Chuyển đổi raw logs (Eve JSON) từ Suricata sang 43 features tương thích với UNSW-NB15 XGBoost.
"""
import json
import logging
import dateutil.parser

logger = logging.getLogger(__name__)

class SuricataParser:
    def __init__(self, feature_names):
        """
        Khởi tạo parser với danh sách 43 features chuẩn của model.
        """
        self.feature_names = feature_names

    def parse_log(self, filepath, max_records=None):
        """
        Đọc file log suricata.json (do Elasticsearch export ra).
        Trả về list các dict, mỗi dict là 1 record chứa 43 features.
        max_records: dừng sớm sau khi đủ số record hợp lệ (None = hết file).
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            logger.error(f"Lỗi khi đọc file log: {e}")
            return []

        if not isinstance(data, list):
            data = [data]

        parsed_records = []
        
        for idx, item in enumerate(data):
            try:
                # Trích xuất event.original (chứa raw Suricata JSON string)
                if "_source" in item and "event.original" in item["_source"]:
                    raw_str = item["_source"]["event.original"]
                elif "fields" in item and "event.original" in item["fields"]:
                    # The value is a list of strings; take the first one.
                    raw_str = item["fields"]["event.original"][0]
                else:
                    logger.warning(f"Bỏ qua record #{idx}: không tìm thấy event.original")
                    continue
                
                eve_log = json.loads(raw_str)
                features = self._extract_features(eve_log)
                parsed_records.append({
                    "original_log": eve_log,
                    "features": features
                })
                if max_records and len(parsed_records) >= max_records:
                    logger.info(
                        f"Đã lấy đủ {max_records} record hợp lệ, dừng parse sớm."
                    )
                    break
            except Exception as e:
                logger.warning(f"Lỗi parse record #{idx}: {e}")
                
        return parsed_records

    def _extract_features(self, eve_log):
        """
        Ánh xạ các trường từ Suricata EVE log sang 43 features của UNSW-NB15.
        """
        # Khởi tạo vector với giá trị 0
        feat = {k: 0.0 for k in self.feature_names}
        
        # 1. Các thông tin cơ bản
        feat['source_port'] = eve_log.get('src_port', 0)
        feat['destination_port'] = eve_log.get('dest_port', 0)
        
        # Protocol (categorical) - đưa về string chữ thường
        proto = eve_log.get('proto', 'tcp').lower()
        feat['protocol'] = proto
        
        # Service (categorical) - HTTP, DNS, FTP, etc.
        app_proto = eve_log.get('app_proto', '-')
        if app_proto == 'failed':
            app_proto = '-'
        feat['service'] = app_proto.lower()
        
        # State (categorical) - Suricata ít khi log cụ thể TCP state cho mọi flow,
        # Nếu không có thì để mặc định 'CON' (Connected) hoặc 'INT' (Interrupted)
        feat['state'] = 'con'
        if 'tcp' in eve_log and 'state' in eve_log['tcp']:
            feat['state'] = eve_log['tcp']['state'].lower()
            
        # 2. Flow stats (Rất quan trọng)
        if 'flow' in eve_log:
            flow = eve_log['flow']
            
            # Packets & Bytes
            feat['spkts'] = flow.get('pkts_toserver', 0)
            feat['dpkts'] = flow.get('pkts_toclient', 0)
            feat['sbytes'] = flow.get('bytes_toserver', 0)
            feat['dbytes'] = flow.get('bytes_toclient', 0)
            
            # Tính Duration (dur)
            try:
                if 'start' in flow and 'timestamp' in eve_log:
                    start_time = dateutil.parser.parse(flow['start'])
                    end_time = dateutil.parser.parse(eve_log['timestamp'])
                    dur = (end_time - start_time).total_seconds()
                    feat['dur'] = dur if dur > 0 else 0.001
            except:
                feat['dur'] = 0.1
                
            # Tính Load (bits/second)
            if feat['dur'] > 0:
                feat['sload'] = (feat['sbytes'] * 8) / feat['dur']
                feat['dload'] = (feat['dbytes'] * 8) / feat['dur']
                
            # Tính Packet rate (sintpkt, dintpkt)
            if feat['spkts'] > 1:
                feat['sintpkt'] = (feat['dur'] * 1000) / feat['spkts']
            if feat['dpkts'] > 1:
                feat['dintpkt'] = (feat['dur'] * 1000) / feat['dpkts']
                
            # Tính Packet size mean
            if feat['spkts'] > 0:
                feat['smeansz'] = feat['sbytes'] / feat['spkts']
            if feat['dpkts'] > 0:
                feat['dmeansz'] = feat['dbytes'] / feat['dpkts']
                
        # 3. HTTP chuyên sâu (nếu có)
        if 'http' in eve_log:
            feat['trans_depth'] = 1
            feat['res_bdy_len'] = eve_log['http'].get('length', 0)
            
        # Các features toán học phức tạp khác (jitter, tcp base seq, window size...)
        # Suricata không cung cấp mặc định trong bản build chuẩn.
        # Chúng ta đã khởi tạo 0.0 cho tất cả, điều này an toàn cho pipeline production POC.
        
        # Chuyển đổi thành một dictionary theo đúng thứ tự (Categorical vẫn là chuỗi)
        return feat
