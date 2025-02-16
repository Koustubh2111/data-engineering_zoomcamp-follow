```console
prefect server start
```

```console
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
prefect init
prefect worker start -p [worker-pool-name]
prefect deploy -n [deployment name]
prefect deployment run 'file.py:flow_entrypoint'
```