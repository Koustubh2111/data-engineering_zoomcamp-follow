1. Start the prefect server - Following is using Prefect v3
```console
prefect server start
```

2. In another terminal, set the PREFECT_API_URL env var to local prefect server. Prefect init creates a prefect.yaml file, just running prefect init gives the interactive mode to choose any recipie (S3, local, docker etc). Once the YAML is edited to required configurations, start a worker in a new worker pool. The process worker pool is created in the UI.
```console
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
prefect init
prefect worker start -p [worker-pool-name]
```

3. Deploy the YAML file using prefect deploy and the name used in the YAML file. This schedules a run in the worker pool. prefect deployment run is only necessary to run the flow immediately. A schedule can be given in the YAML file for auto runs.
```console
prefect deploy -n [deployment name]
prefect deployment run 'file.py:flow_entrypoint'
```

4. Create a docker file from prefecthq/prefect:3.2.2, required libraries are installed from [docker-requirements](./docker-requirements.txt) , flow codes and data are copied. Execute the following commands
```console
docker image build -t [docker-hub-username]/prefectw2:zoomcamp .
docker image push [docker-hub-username]/prefectw2:zoomcamp
```