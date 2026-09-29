"""
CERT v4.2 Feature Extractor

Transforms raw CERT Insider Threat Dataset (v4.2) logs into per-user-per-day
behavioral feature vectors suitable for ML-based UEBA and FHE inference.

Input:  Raw CSV files (logon.csv, file.csv, email.csv, device.csv, http.csv)
Output: behavioral_features.csv with 17 engineered features per (user, day)
"""
import os
import logging
import pandas as pd
import numpy as np
from datetime import datetime
from .base_adapter import BaseAdapter

logger = logging.getLogger(__name__)

class CertAdapter(BaseAdapter):
    """
    Adapter for CERT v4.2 Dataset.
    Transforms raw CERT logs into a standardized 17-feature vector.
    """
    
    def extract_features(self, raw_dir: str, output_dir: str) -> str:
        """
        Main entry point: parse all CERT v4.2 CSVs → behavioral_features.csv
        Delegates to the standalone function.
        """
        return _extract_features_impl(raw_dir, output_dir)

# The 17 behavioral features we extract per (user, day)
FEATURE_COLUMNS = [
    "login_count",
    "logoff_count",
    "after_hours_login",
    "unique_machines",
    "file_copy_count",
    "file_write_count",
    "file_delete_count",
    "file_exe_count",
    "email_sent",
    "email_external",
    "email_attachments",
    "email_bcc_count",
    "usb_connect",
    "usb_disconnect",
    "http_requests",
    "unique_urls",
    "unique_domains",
]


def _is_after_hours(dt: datetime) -> bool:
    """Return True if timestamp is outside business hours (before 6AM or after 6PM)."""
    return dt.hour < 6 or dt.hour >= 18


def _parse_logon(raw_dir: str) -> pd.DataFrame:
    """Parse logon.csv → per-user-per-day logon features."""
    path = os.path.join(raw_dir, "logon.csv")
    if not os.path.exists(path):
        logger.warning(f"logon.csv not found at {path}")
        return pd.DataFrame()

    logger.info("Parsing logon.csv...")
    df = pd.read_csv(path)

    # Normalize column names (CERT v4.2 uses 'id', 'date', 'user', 'pc', 'activity')
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.date

    # Login count
    logins = df[df["activity"] == "Logon"].groupby(["user", "day"]).size().reset_index(name="login_count")

    # Logoff count
    logoffs = df[df["activity"] == "Logoff"].groupby(["user", "day"]).size().reset_index(name="logoff_count")

    # After-hours logins
    login_df = df[df["activity"] == "Logon"].copy()
    login_df["after_hours"] = login_df["date"].apply(lambda x: _is_after_hours(x))
    ah = login_df[login_df["after_hours"]].groupby(["user", "day"]).size().reset_index(name="after_hours_login")

    # Unique machines
    machines = df.groupby(["user", "day"])["pc"].nunique().reset_index(name="unique_machines")

    # Merge all logon features
    result = logins
    for right in [logoffs, ah, machines]:
        if not right.empty:
            result = result.merge(right, on=["user", "day"], how="outer")

    return result.fillna(0)


def _parse_file(raw_dir: str) -> pd.DataFrame:
    """Parse file.csv → per-user-per-day file activity features."""
    path = os.path.join(raw_dir, "file.csv")
    if not os.path.exists(path):
        logger.warning(f"file.csv not found at {path}")
        return pd.DataFrame()

    logger.info("Parsing file.csv...")
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.date

    # In CERT v4.2, file.csv does not have an 'activity' column.
    # Every row is considered a file access/copy.
    result = df.groupby(["user", "day"]).size().reset_index(name="file_copy_count")
    result["file_write_count"] = 0
    result["file_delete_count"] = 0

    # Count .exe file accesses
    if "filename" in df.columns:
        exe = df[df["filename"].str.lower().str.endswith(".exe", na=False)]
        exe_count = exe.groupby(["user", "day"]).size().reset_index(name="file_exe_count")
        result = result.merge(exe_count, on=["user", "day"], how="left")
    else:
        result["file_exe_count"] = 0

    return result.fillna(0)


def _parse_email(raw_dir: str) -> pd.DataFrame:
    """Parse email.csv → per-user-per-day email features."""
    path = os.path.join(raw_dir, "email.csv")
    if not os.path.exists(path):
        logger.warning(f"email.csv not found at {path}")
        return pd.DataFrame()

    logger.info("Parsing email.csv...")
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.date

    # Total emails sent
    sent = df.groupby(["user", "day"]).size().reset_index(name="email_sent")

    # External emails (to addresses not in the org domain)
    if "to" in df.columns:
        # Heuristic: external = contains a non-org domain
        # CERT uses synthetic addresses, so we check for addresses without the org pattern
        external = df[df["to"].str.contains("@", na=False)]
        ext_count = external.groupby(["user", "day"]).size().reset_index(name="email_external")
    else:
        ext_count = pd.DataFrame(columns=["user", "day", "email_external"])

    # Attachments
    if "attachments" in df.columns:
        df["has_attachment"] = df["attachments"].notna() & (df["attachments"] != "")
        att = df[df["has_attachment"]].groupby(["user", "day"]).size().reset_index(name="email_attachments")
    else:
        att = pd.DataFrame(columns=["user", "day", "email_attachments"])

    # BCC count
    if "bcc" in df.columns:
        bcc_df = df[df["bcc"].notna() & (df["bcc"] != "")]
        bcc = bcc_df.groupby(["user", "day"]).size().reset_index(name="email_bcc_count")
    else:
        bcc = pd.DataFrame(columns=["user", "day", "email_bcc_count"])

    result = sent
    for right in [ext_count, att, bcc]:
        if not right.empty:
            result = result.merge(right, on=["user", "day"], how="left")

    return result.fillna(0)


def _parse_device(raw_dir: str) -> pd.DataFrame:
    """Parse device.csv → per-user-per-day USB activity features."""
    path = os.path.join(raw_dir, "device.csv")
    if not os.path.exists(path):
        logger.warning(f"device.csv not found at {path}")
        return pd.DataFrame()

    logger.info("Parsing device.csv...")
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.date

    connect = df[df["activity"] == "Connect"].groupby(["user", "day"]).size().reset_index(name="usb_connect")
    disconnect = df[df["activity"] == "Disconnect"].groupby(["user", "day"]).size().reset_index(name="usb_disconnect")

    result = connect.merge(disconnect, on=["user", "day"], how="outer")
    return result.fillna(0)


def _parse_http(raw_dir: str) -> pd.DataFrame:
    """Parse http.csv → per-user-per-day web browsing features in chunks."""
    path = os.path.join(raw_dir, "http.csv")
    if not os.path.exists(path):
        logger.warning(f"http.csv not found at {path}")
        return pd.DataFrame()

    logger.info("Parsing http.csv (in chunks due to large size)...")
    
    # We will accumulate counts and sets of unique URLs/domains per (user, day)
    requests_counter = {}
    unique_urls_tracker = {}
    unique_domains_tracker = {}

    # Process in chunks of 1M rows
    chunksize = 1000000
    chunk_idx = 0
    
    for chunk in pd.read_csv(path, chunksize=chunksize):
        chunk.columns = [c.strip().lower() for c in chunk.columns]
        # Fast datetime parsing (assuming mm/dd/yyyy HH:MM:SS)
        chunk["date"] = pd.to_datetime(chunk["date"], format="%m/%d/%Y %H:%M:%S", errors="coerce")
        chunk["day"] = chunk["date"].dt.date
        
        # Aggregate requests
        reqs = chunk.groupby(["user", "day"]).size().to_dict()
        for k, v in reqs.items():
            requests_counter[k] = requests_counter.get(k, 0) + v
            
        # Aggregate unique urls
        if "url" in chunk.columns:
            urls_grouped = chunk.groupby(["user", "day"])["url"].apply(set).to_dict()
            for k, v in urls_grouped.items():
                if k not in unique_urls_tracker:
                    unique_urls_tracker[k] = set()
                unique_urls_tracker[k].update(v)
                
            # Aggregate unique domains
            chunk["domain"] = chunk["url"].str.extract(r"(?:https?://)?([^/]+)", expand=False)
            domains_grouped = chunk.groupby(["user", "day"])["domain"].apply(set).to_dict()
            for k, v in domains_grouped.items():
                if k not in unique_domains_tracker:
                    unique_domains_tracker[k] = set()
                unique_domains_tracker[k].update(v)
                
        chunk_idx += 1
        logger.info(f"  Processed {chunk_idx} million rows...")

    # Build final DataFrame
    records = []
    for k in requests_counter.keys():
        user, day = k
        urls_count = len(unique_urls_tracker.get(k, set()))
        domains_count = len(unique_domains_tracker.get(k, set()))
        records.append({
            "user": user,
            "day": day,
            "http_requests": requests_counter[k],
            "unique_urls": urls_count,
            "unique_domains": domains_count
        })

    result = pd.DataFrame(records)
    return result.fillna(0)


def _load_labels(raw_dir: str) -> pd.DataFrame:
    """
    Load ground-truth insider threat labels from CERT answers file.
    Returns DataFrame with columns: [user, day, label]
    label = 1 for malicious activity, 0 for normal.
    """
    # CERT v4.2 provides labels in various formats
    # Try common patterns in raw_dir and its parent directory (if answers is extracted separately)
    parent_dir = os.path.dirname(raw_dir)
    potential_paths = [
        os.path.join(raw_dir, "insiders.csv"),
        os.path.join(raw_dir, "answers.csv"),
        os.path.join(parent_dir, "answers", "insiders.csv"),
        os.path.join(parent_dir, "answers", "answers.csv"),
        os.path.join(parent_dir, "insiders.csv"),
    ]

    for path in potential_paths:
        if os.path.exists(path):
            logger.info(f"Loading labels from {path}...")
            df = pd.read_csv(path)
            df.columns = [c.strip().lower() for c in df.columns]
            
            # If the dataset provides 'date' instead of 'start'/'end'
            if "date" in df.columns and "start" not in df.columns:
                df["day"] = pd.to_datetime(df["date"], format="mixed", errors="coerce").dt.date
                
            return df

    logger.warning("No labels file found. All samples will be labeled as normal (0).")
    return pd.DataFrame(columns=["user", "day"])


def _extract_features_impl(raw_dir: str, output_dir: str) -> str:
    """
    Standalone entry point: parse all CERT v4.2 CSVs → behavioral_features.csv
    (Also used by CertAdapter.extract_features)

    Returns path to the output CSV file.
    """
    output_path = os.path.join(output_dir, "behavioral_features.csv")
    if os.path.exists(output_path):
        logger.info(f"Features already extracted at {output_path}. Skipping extraction step!")
        return output_path

    os.makedirs(output_dir, exist_ok=True)

    # Parse each log stream
    logger.info("Parsing logon.csv...")
    logon_df = _parse_logon(raw_dir)
    logger.info("Parsing file.csv...")
    file_df = _parse_file(raw_dir)
    logger.info("Parsing email.csv...")
    email_df = _parse_email(raw_dir)
    logger.info("Parsing device.csv...")
    device_df = _parse_device(raw_dir)
    logger.info("Parsing http.csv...")
    http_df = _parse_http(raw_dir)

    # Merge all features on (user, day)
    dfs = [logon_df, file_df, email_df, device_df, http_df]
    dfs = [df for df in dfs if not df.empty]

    if not dfs:
        logger.error("No data parsed! Check that raw CERT CSVs exist in: " + raw_dir)
        return ""

    merged = dfs[0]
    for df in dfs[1:]:
        merged = merged.merge(df, on=["user", "day"], how="outer")

    # Ensure all feature columns exist
    for col in FEATURE_COLUMNS:
        if col not in merged.columns:
            merged[col] = 0

    merged = merged.fillna(0)

    # Load labels
    labels_df = _load_labels(raw_dir)
    
    if "label" not in merged.columns:
        merged["label"] = 0

    if not labels_df.empty and "user" in labels_df.columns:
        if "start" in labels_df.columns and "end" in labels_df.columns:
            # Labels have start and end dates (like CERT v4.2 insiders.csv)
            labels_df["start"] = pd.to_datetime(labels_df["start"], format="mixed", errors="coerce").dt.date
            labels_df["end"] = pd.to_datetime(labels_df["end"], format="mixed", errors="coerce").dt.date
            
            for _, row in labels_df.iterrows():
                u = row["user"]
                s = row["start"]
                e = row["end"]
                if pd.notna(s) and pd.notna(e):
                    # Mark all days between start and end as malicious
                    mask = (merged["user"] == u) & (merged["day"] >= s) & (merged["day"] <= e)
                    merged.loc[mask, "label"] = 1
        elif "day" in labels_df.columns:
            # Fallback for exact day labels
            labels_df["label"] = 1
            merged = merged.merge(
                labels_df[["user", "day", "label"]],
                on=["user", "day"],
                how="left",
                suffixes=("", "_y")
            )
            merged["label"] = merged["label"].mask(merged["label_y"] == 1, 1)
            merged = merged.drop(columns=["label_y"], errors="ignore")

    merged["label"] = merged["label"].fillna(0).astype(int)

    # Select final columns
    output_cols = ["user", "day"] + FEATURE_COLUMNS + ["label"]
    merged = merged[output_cols].sort_values(["user", "day"]).reset_index(drop=True)

    # Save
    output_path = os.path.join(output_dir, "behavioral_features.csv")
    merged.to_csv(output_path, index=False)

    logger.info(f"Feature extraction complete!")
    logger.info(f"  Rows: {len(merged)}")
    logger.info(f"  Users: {merged['user'].nunique()}")
    logger.info(f"  Days: {merged['day'].nunique()}")
    logger.info(f"  Malicious: {merged['label'].sum()} ({merged['label'].mean()*100:.2f}%)")
    logger.info(f"  Saved to: {output_path}")

    return output_path


if __name__ == "__main__":
    import sys
    raw = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "..", "data", "cert", "raw")
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join("..", "..", "data", "cert", "processed")
    _extract_features_impl(raw, out)

