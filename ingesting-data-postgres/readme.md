1. Run the postgres container in the terminal (use full path for volume mount instead of $(pwd)). The network is specified as pg-network along with a name so the pgadmin docker container can also be initialized in future steps in the same network.

```console
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB='hotel_bookings' \
  -v $(pwd)/hotel-bookings-data/hotel_bookings/db_data:/var/lib/postgres/data \   
  -p 5432:5432 \
  --network=pg-network
  --name pgdb
  postgres:latest
```

2. When the database is ready to accept connections, use the pgcli library to connect to the database [^1]

```console
pip install pgcli
pgcli -h localhost -p 5432 -u root -d hotel_bookings
```

3. Once connected, the terminal will look like below

```console
Server: PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)
Version: 4.1.0
Home: http://pgcli.com
hotel_bookings>
```

4. Hotel bookings dataset was downloaded from [kaggle](https://www.kaggle.com/datasets/mathsian/hotel-bookings/data). The downloaded dataset in the [local machine](./hotel-bookings-data/) was mounted to the postgres container volume. The data was ingested to the "hotel_bookings_data" table in the connected postgres database in chunks - [code](data_ingestion.py).

5. A pgadmin docker container is initialized with the same network as the postgres docker. The pgadmin is run using the localhost:8080 URL. In the pgadmin GUI, a new connection is added with the postgres DB name (pgdb) and credentials. This makes it easier to write SQL queries for the data in pgdb.

```console
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin \
 dpage/pgadmin4

```



[^1]: Docker-compose file is unrelated to the data ingestion test. It will be used further along in the course. 