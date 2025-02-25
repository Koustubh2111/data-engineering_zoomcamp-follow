1. DBT is initialzed with big query using dbt init. Link the service account to big query
```console
dbt init
```
2. A DBT folder structure is created
```
├── src/ │ ├── main.py │ ├── utils.py ├── data/ │ ├── raw/ │ ├── processed/ ├── docs/ │ ├── README.md ├── .gitignore ├── requirements.txt ├── setup.py
```