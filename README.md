# Kidney Tumour Detection using Deep Learning
Kidney Disease Classification MLflow DVC

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the main.py
8. Update the dvc.yaml
10.app.py

# How to run ?

### STEPS:

Clone the repository

```bash
https://github.com/kvamsi7/kidney-disease-classification-dl-project
```

### STEP 01 - Create a conda environment after opening the repository
```bash
conda create -n cnnclsfr python=3.8 -y
```

```bash
conda activate cnncls
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

## MLFlow


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = "https://dagshub.com/kvamsi7/kidney-disease-classification-dl-project.mlflow"\
MLFLOW_TRACKING_USERNAME = "username"\
MLFLOW_TRACKING_PASSWORD = "d6b1c8cf96f5b7cc6f735f6e0c8d127e5ad9c82d"\

Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI = "https://dagshub.com/kvamsi7/kidney-disease-classification-dl-project.mlflow"

export MLFLOW_TRACKING_USERNAME = "username"

export MLFLOW_TRACKING_PASSWORD = "d6b1c8cf96f5b7cc6f735f6e0c8d127e5ad9c82d"
```