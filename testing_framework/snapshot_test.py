import json

def snapshot_test(transform_fn, input_data_path, expected_output_path):
    with open(input_data_path) as f:
        input_data = json.load(f)

    with open(expected_output_path) as f:
        expected_output = json.load(f)

    actual_output = transform_fn(input_data)
    assert actual_output == expected_output, f"Mismatch! Expected: {expected_output}, Got: {actual_output}"
    print("Snapshot test passed.")
