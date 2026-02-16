#%% Libraries necessaires
import pandas as pd

# %% Fonction d'enrichissement des données de ventes
def enrich_sales(
    orders: pd.DataFrame,
    products: pd.DataFrame,
    customers: pd.DataFrame
) -> pd.DataFrame:
    """
    Enrichit les commandes avec les données produits et clients
    et calcule le chiffre d'affaires.
    """

    # Jointure orders + products
    df = orders.merge(
        products,
        on="product_id",
        how="left"
    )

    # Jointure avec customers
    df = df.merge(
        customers,
        on="customer_id",
        how="left"
    )

    # Calcul du chiffre d'affaires
    df["revenue"] = df["quantity"] * df["unit_price"]

    # Sélection des colonnes finales
    final_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "customer_name",
        "country",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "revenue",
    ]

    df = df[final_columns]

    return df

# %%
