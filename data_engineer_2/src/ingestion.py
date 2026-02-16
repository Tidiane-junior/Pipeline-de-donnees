#%% Libraries necessaires
import pandas as pd
from pathlib import Path

#%% Fonction pour le chargement des donnees
def load_csv(file_path: Path) -> pd.DataFrame:

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")
    return pd.read_csv(path)
