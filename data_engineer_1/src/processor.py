# Fonction pour valider les données
import pandas as pd

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Vérifie que les colonnes nécessaires sont présentes
    et que les valeurs numériques sont valides.
    """
    required_columns = {"order_id", "price", "quantity"}

    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Colonnes manquantes : {missing}")

    if (df["price"] <= 0).any():
        raise ValueError("Prix négatif ou nul détecté")

    if (df["quantity"] <= 0).any():
        raise ValueError("Quantité négative ou nulle détectée")

    return df

# Fonction pour calculer le chiffre d'affaires
def compute_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajoute une colonne 'revenue' = price * quantity
    """
    df = df.copy()
    df["revenue"] = df["price"] * df["quantity"]
    return df


# Fonction pour traiter un chunk de données
def process_chunk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applique validation et transformation sur chaque chunk.
    """
    from processor import validate_data, compute_revenue

    df = validate_data(df)
    df = compute_revenue(df)

    return df


