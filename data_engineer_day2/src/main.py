# -*- coding: utf-8 -*-
#%% Utiser la fonction "load_csv" de ingestion.py pour charger les fichiers CSV
from ingestion import load_csv
from validation import validate_orders, validate_products, validate_customers

#%% Fonction principale
def main():
    print("Debut du pipeline – Etape ingestion + validation")

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

    # Afficher les résultats
    print("Fichiers chargés et validés avec succès")
    print(f"Orders: {orders.shape}")
    print(f"Products: {products.shape}")
    print(f"Customers: {customers.shape}")


if __name__ == "__main__":
    main()

# %%
