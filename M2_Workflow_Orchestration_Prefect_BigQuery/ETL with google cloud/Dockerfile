FROM prefecthq/prefect:3.2.2-python3.12

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypi.python.org --no-cache-dir

COPY data data/
COPY etl_gcs_to_bq.py etl_gcs_to_bq.py
COPY etl_web_to_gcs.py etl_web_to_gcs.py
COPY parameterizing_flow.py parameterizing_flow.py

