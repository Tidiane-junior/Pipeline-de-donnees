#%% Libraries necessaires
import pandas as pd
from pathlib import Path

#%% Fonction pour le chargement des donnees
def load_csv(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")
    return pd.read_csv(file_path)
