import json
from snapshot_test import snapshot_test

def transform(data):
    return {"metric_a_total": sum(row["amount"] for row in data)}

snapshot_test(transform, "test_data/input.json", "test_data/expected_output.json")
