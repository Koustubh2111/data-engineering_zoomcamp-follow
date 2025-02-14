#### The prefect intro code is doing a basic ETL operation
1. The necessary libraries for the introduction are prefect and prefect-sqlalchemy
```console
pip install prefect, prefect-sqlalchemy
```
2. Extract, transform and load are set as three tasks for prefect main flow. The workflow can be visualized using
```console
prefect server start
```
3. postgres server credentials are used in the code the SQL alchemy connector block