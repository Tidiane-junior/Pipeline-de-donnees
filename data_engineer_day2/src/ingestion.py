#%% Libraries necessaires
import pandas as pd
from pathlib import Path

#%% Fonction pour le chargement des donnees
def load_csv(file_path: str) -> pd.DataFrame:
    """
    Charge un fichier CSV depuis le dossier data/raw.

    Args:
        file_path (str): chemin du fichier CSV

    Returns:
        pd.DataFrame: données chargées
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")

    df = pd.read_csv(path)

    return df
