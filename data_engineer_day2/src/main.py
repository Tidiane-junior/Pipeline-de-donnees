# -*- coding: utf-8 -*-
#%% Utiser la fonction "load_csv" de ingestion.py pour charger les fichiers CSV
from ingestion import load_csv
from validation import validate_orders, validate_products, validate_customers
from enrichir import enrich_sales
from golden import save_dataframe
#%% Fonction principale
def main():
    print("Pipeline – Ingestion → Validation → Enrichissement")

    # Chemins des fichiers CSV
    path_orders = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_day2\\data\\raw\\orders.csv"
    path_products = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_day2\\data\\raw\\products.csv"
    path_customers = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_day2\\data\\raw\\customers.csv"

    # Chargement des fichiers CSV
    orders = load_csv(path_orders)
    products = load_csv(path_products)
    customers = load_csv(path_customers)

    # Validation des données
    orders = validate_orders(orders)
    products = validate_products(products)
    customers = validate_customers(customers)


    sales = enrich_sales(orders, products, customers)

    save_dataframe(
        sales,
        "data/processed/golden.parquet"
    )

    print("✅ Pipeline terminé")
    print(sales.head())
    print(f"Dataset final : {sales.shape}")


if __name__ == "__main__":
    main()

# %%
