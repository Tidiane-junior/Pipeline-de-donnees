from datetime import datetime
from airflow import DAG
# from airflow.operators.python import PythonOperator
from pathlib import Path
import sys

#%% Importer les modules src/
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # remonte à data_engineer_2
SRC_PATH = PROJECT_ROOT / "src"
sys.path.append(str(SRC_PATH))

from data_engineer_2.src.main import run_pipeline  # la fonction qu'on a créée

# def run_pipeline():
