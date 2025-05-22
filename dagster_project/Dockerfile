FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install dagster dagit

CMD ["dagit", "-f", "dagster_pipeline.py", "-h", "0.0.0.0", "-p", "3000"]
