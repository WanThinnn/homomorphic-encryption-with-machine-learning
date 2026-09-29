import os
import logging
import pandas as pd
from .base_adapter import BaseAdapter

logger = logging.getLogger(__name__)

class ElasticEcsAdapter(BaseAdapter):
    """
    Adapter for Elastic Common Schema (ECS) logs.
    This parses JSON lines exported from Elasticsearch/Kibana.
    """

    def extract_features(self, raw_dir: str, output_dir: str) -> str:
        output_path = os.path.join(output_dir, "behavioral_features.csv")
        if os.path.exists(output_path):
            logger.info(f"Features already extracted at {output_path}. Skipping ECS extraction.")
            return output_path

        logger.info("Parsing Elastic ECS logs...")
        
        # We will parse all JSON files in raw_dir
        all_records = []
        for file in os.listdir(raw_dir):
            if file.endswith(".json"):
                file_path = os.path.join(raw_dir, file)
                try:
                    import json
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            for doc in data:
                                fields = doc.get("fields", {})
                                
                                # Extract IP / User (Treating source.ip as "user" for network logs)
                                src_ip = fields.get("source.ip", [None])[0]
                                if not src_ip:
                                    continue
                                
                                # Extract Timestamp -> Day
                                timestamp = fields.get("@timestamp", [None])[0]
                                day = pd.to_datetime(timestamp).date() if timestamp else None
                                
                                # Network features
                                http_req = 1 if "http" in fields.get("network.protocol", []) else 0
                                urls = fields.get("url.original", [])
                                url_count = len(urls)
                                domains = fields.get("url.domain", [])
                                domain_count = len(domains)
                                
                                # File features (Looking for .exe in Suricata logs)
                                exe_count = 1 if any(".exe" in str(p) for p in fields.get("url.path", [])) else 0
                                
                                # Assemble record
                                record = {
                                    "user": src_ip,
                                    "day": day,
                                    "login_count": 0, "logoff_count": 0, 
                                    "file_copy_count": 0, "file_write_count": 0, 
                                    "file_delete_count": 0, "file_exe_count": exe_count,
                                    "email_sent_count": 0, "email_external_count": 0, 
                                    "email_attachment_count": 0, "email_size_mean": 0,
                                    "http_requests": http_req, 
                                    "unique_urls": url_count, 
                                    "unique_domains": domain_count,
                                    "device_connect_count": 0, 
                                    "device_disconnect_count": 0,
                                    "label": 0  # Default to normal, need external labeling for real data
                                }
                                all_records.append(record)
                except Exception as e:
                    logger.error(f"Error reading {file_path}: {e}")

        # Aggregate by User and Day
        if all_records:
            df = pd.DataFrame(all_records)
            df = df.groupby(["user", "day"]).agg({
                "login_count": "sum", "logoff_count": "sum", 
                "file_copy_count": "sum", "file_write_count": "sum", 
                "file_delete_count": "sum", "file_exe_count": "sum",
                "email_sent_count": "sum", "email_external_count": "sum", 
                "email_attachment_count": "sum", "email_size_mean": "mean",
                "http_requests": "sum", 
                "unique_urls": "sum", 
                "unique_domains": "sum",
                "device_connect_count": "sum", 
                "device_disconnect_count": "sum",
                "label": "max"
            }).reset_index()
            # Fill NaN
            df.fillna(0, inplace=True)
        else:
            # Fallback empty dataframe if no logs
            cols = [
                "user", "day", "login_count", "logoff_count", "file_copy_count", 
                "file_write_count", "file_delete_count", "file_exe_count", 
                "email_sent_count", "email_external_count", "email_attachment_count", 
                "email_size_mean", "http_requests", "unique_urls", "unique_domains", 
                "device_connect_count", "device_disconnect_count", "label"
            ]
            df = pd.DataFrame(columns=cols)
        
        os.makedirs(output_dir, exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"ECS parsing complete. Extracted {len(df)} daily user profiles. Saved to {output_path}")
        return output_path
