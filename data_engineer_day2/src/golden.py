from pathlib import Path
import pandas as pd


def save_dataframe(
    df: pd.DataFrame,
    output_path: str,
    index: bool = False
) -> None:
    """
    Sauvegarde un DataFrame dans le dossier processed.
    """
    path = Path(output_path)

    # Création du dossier si nécessaire
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(path, index=index)

