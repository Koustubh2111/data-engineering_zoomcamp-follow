1. Run the postgres container in the terminal (use full path for volume mount instead of $(pwd))

```console
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB='hotel_bookings' \
  -v $(pwd)/hotel-bookings-data/hotel_bookings:var/lib/postgres/data \   
  -p 5432:5432 \
  postgres:latest
```
2. When the database is ready to accept connections, use the pgcli library to connect to the database

```console
pip install pgcli
pgcli -h localhost -p 5432 -u root -d hotel_bookings
```

3. Once connect, the terminal will look like below

```console
Server: PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)
Version: 4.1.0
Home: http://pgcli.com
hotel_bookings>
```
### Docker-compose file is unrelated to the data ingestion test. It will be used further along in the course. 