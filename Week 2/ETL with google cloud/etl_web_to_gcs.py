from pathlib import Path
import pandas as pd
from prefect import task, flow
from prefect_gcp.cloud_storage import GcsBucket


@task(retries=3)
def get_data(url: str) -> pd.DataFrame:
    """Reads green taxi data from the url"""
    return pd.read_csv(url)

@task(log_prints=True)
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Fixes data types and masks cateforical inputs"""

    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
    df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

    df['store_and_fwd_flag'] = df['store_and_fwd_flag'].map({'Y' : 1, 'N' : 0})

    print(df.head(2))
    print(f'Columns : {df.dtypes}')
    print(f'Rows : {len(df)}')

    return df

@task(log_prints=True)
def write_local(df: pd.DataFrame, color: str, dataset_file: str) -> Path:
    """Write dataframe to parquet file"""

    path = Path(f'data/{color}/{dataset_file}')
    df.to_parquet(path, compression='gzip')
    return path

@task()
def write_gcs(path: Path) -> None:
    """Write local parquet file to GCS"""
    gcs_bucket_block = GcsBucket.load("de-zoomcamp-week2")
    gcs_bucket_block.upload_from_path(from_path=path, to_path=path)


@flow()
def etl_gcs_to_web() -> None:
    """Main ETL flow"""
    color = "green"
    year = 2019
    month = 1

    dataset_file = f'{color}_tripdata_{year}-{month:02}'
    dataset_url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz'

    df = get_data(dataset_url)
    df_clean = clean_data(df)
    path = write_local(df_clean, color, dataset_file)
    write_gcs(path)

if __name__ == "__main__":
    etl_gcs_to_web()
