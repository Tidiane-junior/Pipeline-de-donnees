#  Installer les packages si besoin
# pip install pyarrow

# Importer les modules nécessaires
import logging # Importation du module de logging pour la gestion des logs
from pathlib import Path # Importer Path pour la gestion des chemins de fichiers
import pandas as pd

# Fonction pour configurer le logger
def setup_logger():
    """
    Configure le système de logs du projet.
    Les logs sont écrits dans un fichier avec date et niveau.
    Ils servent à :
        - comprendre ce qui s’est passé
        - diagnostiquer une erreur
        - tracer l’exécution d’un pipeline

    """
    
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=log_dir / "pipeline.log", # Fichier de log pour stocker les messages de log
        level=logging.INFO, # Le niveau de log est défini sur INFO pour capturer les messages d'information
        format="%(asctime)s - %(levelname)s - %(message)s" # Format des messages de log avec la date, le niveau et le message
    )

    return logging.getLogger(__name__)


# Fonction pour écrire un DataFrame au format Parquet
def write_parquet(df: pd.DataFrame, output_path: str):
    """
    Écrit un DataFrame au format Parquet.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(path, index=False)