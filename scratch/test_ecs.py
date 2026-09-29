import os
import sys
import logging
logging.basicConfig(level=logging.INFO)

from src.data.adapters.elastic_ecs_adapter import ElasticEcsAdapter

if os.path.exists('tmp/ecs_test/behavioral_features.csv'):
    os.remove('tmp/ecs_test/behavioral_features.csv')

adapter = ElasticEcsAdapter()
out_csv = adapter.extract_features('logs', 'tmp/ecs_test')

import pandas as pd
df = pd.read_csv(out_csv)
print("\n=== EXTRACTED FEATURES ===")
print(df.to_string())
