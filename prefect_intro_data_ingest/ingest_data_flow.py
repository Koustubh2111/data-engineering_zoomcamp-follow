import pandas as pd
from sqlalchemy import create_engine
from time import time
from prefect import flow, task


@task(log_prints = True)
def extract_data(csv_file, chunksize = 1000):

    return pd.read_csv(csv_file)


@task(log_prints = True)
def transform_data(df):

    #Combine three timestamp columns into one 
    df = df.rename(columns={'arrival_date_day_of_month': 'day', 'arrival_date_month': 'month',\
                             'arrival_date_year': 'year'})
    df['month'] = pd.to_datetime(df['month'], format = "%B").dt.month
    timestamp_cols = ['year', 'month', 'day']
    df['arrival_timestamp'] = pd.to_datetime(df[timestamp_cols])
    df.drop(timestamp_cols, axis = 1, inplace = True)

    #Rearrange cols
    timestamp = df.pop('arrival_timestamp')
    df.insert(3, 'arrival_timestamp', timestamp)

    #remove fields with days_in_waiitng_list < 50 and previous_bookings_not_cancelled > 50
    #Arbitrary transformation
    return df[(df['days_in_waiting_list'] < 50) & (df['previous_bookings_not_canceled'] > 50)].reset_index()


@task(log_prints=True, retries=3)
def load_data(user,password,host, port, db, table_name, df):

    '''
    task decorator used for metadata and upstream dependencies 
    '''

    #Create the SQL engine
    #Use postgresql in the URL and not postgres
    postgres_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = create_engine(postgres_url)

    #Add to table with 'name' - take care to not use dashes in the name.
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

    #Add the data
    df.to_sql(name=table_name, con=engine, if_exists='append')

@flow(name='Ingest_flow')
def main_flow():
    user = 'root'
    password = 'root'
    host = 'localhost'
    port = '5432'
    db = 'hotel_bookings'
    table_name = 'hotel_bookings_data'
    csv_file = '../ingesting-data-postgres/hotel-bookings-data/hotel_bookings.csv'

    
    raw_data = extract_data(csv_file=csv_file)
    transformed_data = transform_data(raw_data)
    load_data(user,password,host, port, db, table_name, transformed_data)


if __name__ == '__main__':
    main_flow()