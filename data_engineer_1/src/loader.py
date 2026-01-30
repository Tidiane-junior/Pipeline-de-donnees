# Installer les packages si nécessaire
# !pip install pandas

# Importer les modules nécessaires
import pandas as pd
from pathlib import Path
from typing import Iterator # pour le typage des fonctions

# Définir les fonctions de chargement des données

## Fonction pour charger un CSV complet puis retourner un DataFrame
def load_csv(file_path: str) -> pd.DataFrame:
    """
    Charge un fichier CSV et retourne un DataFrame.
    Lève une erreur claire si le fichier est invalide.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")

    df = pd.read_csv(path)
    return df


# Une fonction pour charger un CSV par morceaux (chunks)
def load_csv_in_chunks(
    file_path: str,
    chunksize: int = 2
) -> Iterator[pd.DataFrame]:
    
    """
    Charge un CSV par morceaux (chunks).
    Retourne un itérateur de DataFrames.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")

    return pd.read_csv(path, chunksize=chunksize)

# %%
