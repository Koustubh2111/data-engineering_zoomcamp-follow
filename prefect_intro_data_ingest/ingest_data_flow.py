import pandas as pd
from sqlalchemy import create_engine
from time import time
from prefect import flow, task

@task(log_prints=True, retries=3)
def ingest_date(user,password,host, port, db, table_name, csv_file):

    '''
    Task used with metadata and upstream dependencies 
    '''

    df_iter = pd.read_csv(csv_file, iterator=True, \
                      chunksize=10000)
    
    #Create the SQL engine
    #Use postgresql in the URL and not postgres
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    #Add the header to the database
    df = next(df_iter)
    #Add to table with 'name' - take care to not use dashes in the name.
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

    '''

    #Ingest each of the chunks into the sql table using append
    chunk = 0
    while True:

        try:
            chunk += 1

            start_time = time()

            df = next(df_iter)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            end_time = time()

            print(f'Chunk {chunk} inserted - time : %.3f' % (end_time-start_time))

        except:
            print('End of file reached')
            break
            
    '''

@flow(name='Ingest_flow')
def main_flow():
    user = 'root'
    password = 'root'
    host = 'localhost'
    port = '5432'
    db = 'hotel_bookings'
    table_name = 'hotel_bookings_data'
    csv_file = '../ingesting-data-postgres/hotel-bookings-data/hotel_bookings.csv'

    ingest_date(user,password,host, port, db, table_name, csv_file)


if __name__ == '__main__':
    main_flow()