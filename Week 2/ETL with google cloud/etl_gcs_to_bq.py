from pathlib import Path
import pandas as pd
from prefect import task, flow
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(
        log_prints=True,
        cache_key_fn=task_input_hash,
        cache_expiration=timedelta(days=1)
    )
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    "Download green trip data from GCS - Note that in gcs.get_directory, from path is appended to local path"
    gcs_path = f'data/{color}/'
    print(f'GCS Path : {gcs_path}')
    gcs_bucket_block = GcsBucket.load("de-zoomcamp-week2")
    gcs_bucket_block.get_directory(from_path=gcs_path, local_path=f"./")
    print(f'Returned path : data/{color}/{color}_tripdata_{year}-{month:02}')
    return Path(f'data/{color}/{color}_tripdata_{year}-{month:02}')

@task()
def read_file_locally(path: Path) -> pd.DataFrame:
    """Read the file after itb was extracted from GCS bucket"""
    return pd.read_parquet(path)

@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write dataframe to big query"""

    gcp_credentials_block = GcpCredentials.load("de-zoomcamp-week2")
    
    df.to_gbq(
        destination_table= 'de-zoomcamp-follow-project.de_zoomcamp_w2.rides',
        project_id='de-zoomcamp-follow-project',
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists='append'
    )



@flow()
def etl_gcs_to_bq() -> None:
    "Move data from GCS Bucket to BigQuery"
    color = 'green'
    year = 2019
    month = 1

    path = extract_from_gcs(color, year, month)
    df = read_file_locally(path)
    write_bq(df)


