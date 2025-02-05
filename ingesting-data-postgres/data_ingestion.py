import pandas as pd
from sqlalchemy import create_engine
from time import time


#Chunk the data and return the iterator
df_iter = pd.read_csv('./hotel-bookings-data/hotel_bookings.csv', iterator=True, \
                      chunksize=10000)


#Create the SQL engine
#Use postgresql in the URL and not postgres
engine = create_engine('postgresql://root:root@localhost:5432/hotel_bookings')

#Add the header to the database
df = next(df_iter)
#Add to table with 'name' - take care to not use dashes in the name.
df.head(0).to_sql(name='hotel_bookings_data', con=engine, if_exists='replace')

#Ingest each of the chunks into the sql table using append
chunk = 0
while True:

    try:
        chunk += 1

        start_time = time()

        df = next(df_iter)

        df.to_sql(name='hotel_bookings_data', con=engine, if_exists='append')

        end_time = time()

        print(f'Chunk {chunk} inserted - time : %.3f' % (end_time-start_time))

    except:
        print('End of file reached')
        break

