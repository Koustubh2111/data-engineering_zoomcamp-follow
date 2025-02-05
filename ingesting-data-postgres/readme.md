## To run the postgres container in the terminal

```console
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB='hotel_bookings' \
  -v $(pwd)/hotel-bookings-data/hotel_bookings:var/lib/postgres/data \   #use full path for volume mount
  -p 5432:5432 \
  postgres:latest
```

## Docker-compose file is unrelated to the data ingestion test. It will be used further along in the course. 