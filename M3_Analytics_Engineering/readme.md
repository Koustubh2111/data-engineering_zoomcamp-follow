1. DBT is initialzed with big query using dbt init. Link the service account to big query
```console
dbt init
```
2. A DBT [folder structure](./dbt_starter/) is created with directories for macros, models, seeds and tests. 

3. In order to generate the yml model components for different models, get the codegen package and add it to [packages.yml](./dbt_starter/packages.yml). Run the dbt deps command to install the package and run the generate_model_yaml function. Copy the model components from the terminal to the appropriate schema file.
```console
    dbt deps
    dbt run-operation generate_model_yaml --args '{"model_names":["staging_green_trip_21_3_data", "staging_green_trip_21_5_data"]}'
```

4. Once the model components, tests such as unique, not_null and relationships can be added to the columns. dbt run-operation command can be used to the models in the core folder as well.

5. The documentation along with lineage can be seen by self hosting, dbt docs generate builds the catalog
```console
dbt docs serve
```