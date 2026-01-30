from pathlib import Path
import pandas as pd

# Fonction pour sauvegarder un DataFrame
def save_dataframe(
    df: pd.DataFrame,
    output_path: str,
    index: bool = False
) -> None:
    """
    Sauvegarde un DataFrame dans le dossier processed.
    Args:
        df (pd.DataFrame): Le DataFrame à sauvegarder.
        output_path (str): Le chemin de sortie pour le fichier Parquet.
        index (bool): Indique si l'index doit être sauvegardé. Par défaut à False.
    """
    # Conversion du chemin en objet Path
    path = Path(output_path)

    # Création du dossier si nécessaire
    path.parent.mkdir(parents=True, exist_ok=True)

    # Sauvegarde du DataFrame
    df.to_parquet(path, index=index)

