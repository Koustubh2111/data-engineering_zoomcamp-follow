from pathlib import Path
import pandas as pd
from prefect import task, flow
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


from etl_gcs_to_bq import extract_from_gcs, read_file_locally, write_bq
from etl_web_to_gcs import get_data, clean_data, write_gcs, write_local

@flow()
def dump_to_gcs(
    color: str,
    year: int,
    month: int
) -> None:
    """Subflow 1- Move parquet files to GCS storage bucket"""

    dataset_file = f'{color}_tripdata_{year}-{month:02}'
    dataset_url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz'

    df = get_data(dataset_url)
    df_clean = clean_data(df)
    path = write_local(df_clean, color, dataset_file)
    write_gcs(path)


@flow()
def etl_gcs_to_bq_subflow(
        color: str,
        year: int,
        month: int
)-> None:
    "Subflow 2- Move data from GCS Bucket to BigQuery"

    path = extract_from_gcs(color, year, month)
    df = read_file_locally(path)
    write_bq(df)

@flow()
def etl_parent_flow(
    color: str,
    year: int,
    months: list[int]
) -> None:
    "Parent flow that runs the above subflow for three different months"

    for month in months:

        #Get data from web and move to GCS bucket
        dump_to_gcs(color, year, month)

        #Move from GCS bucket to local again and to BigQuery
        etl_gcs_to_bq_subflow(color, year, month)

if __name__ == "__main__":
    color = 'green'
    year = 2021
    months = [3,4,5]
    etl_parent_flow(color, year, months)
