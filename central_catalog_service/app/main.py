from fastapi import FastAPI

app = FastAPI()

@app.get("/catalog/{metric_name}")
def get_catalog(metric_name: str):
    return {
        "input": f"s3://mock-bucket/input/{metric_name}.csv",
        "output": f"s3://mock-bucket/output/{metric_name}.csv",
        "schema": {"amount": "int"}
    }
