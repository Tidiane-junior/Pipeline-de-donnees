#%% Description: Module de validation des donnees
'''
S’assurer que les données :

    - respectent le schéma attendu
    - ne contiennent pas de valeurs absurdes
    - sont exploitables avant tout calcul ou jointure

    Objectif : Détecter les erreurs le plus tôt possible.
'''
#%% Règles qu’on applique (simples mais pro)
'''
- Pour la table "orders"
    - pas de valeurs nulles sur les clés
    - quantity > 0
    - unit_price >= 0

- Pour la table "products"

    - product_id unique
    - price >= 0
    - pas de catégorie vide

- Pour la table "customers"

    - customer_id unique
    - pays non null
    - date valide

'''

#%% Libraries necessaires
import pandas as pd

#%% Fonctions de validation des données transactionnelles
def validate_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validation des données de commandes.
    """
    # Liste des colonnes requises pour la table orders
    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "quantity",
        "unit_price",
    ]

    # Vérification du schéma
    # Voir si des colonnes sont manquantes en comparant avec la liste requise 
    # à liste des colonnes du DataFrame
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Colonnes manquantes dans orders : {missing_cols}")

    # Suppression des lignes invalides
    df = df.dropna(subset=["order_id", "customer_id", "product_id"])
    df = df[df["quantity"] > 0]
    df = df[df["unit_price"] >= 0]

    return df

# %% Fonction de validation des produits
def validate_products(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validation des données produits.
    """
    df = df.dropna(subset=["product_id", "category"])
    df = df[df["price"] >= 0]
    df = df.drop_duplicates(subset="product_id")

    return df

# %% Fonction de validation des clients
def validate_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validation des données clients.
    """
    df = df.dropna(subset=["customer_id", "country"])
    df = df.drop_duplicates(subset="customer_id")

    return df
