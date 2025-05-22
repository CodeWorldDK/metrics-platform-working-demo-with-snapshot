from dagster import job, op

@op
def fetch_data():
    return [{"amount": 100}, {"amount": 200}]

@op
def run_metric(data):
    return {"metric_a_total": sum(r["amount"] for r in data)}

@op
def validate(result):
    assert result["metric_a_total"] > 0
    return result

@op
def persist(result):
    print("Persisted:", result)

@job
def metric_demo_pipeline():
    persist(validate(run_metric(fetch_data())))
