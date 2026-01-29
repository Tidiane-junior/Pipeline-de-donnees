# -*- coding: utf-8 -*-
#%% Utiser la fonction "load_csv" de ingestion.py pour charger les fichiers CSV
from ingestion import load_csv

#%% Fonction principale
def main():
    print("Debut du pipeline – Etape ingestion")

    path_orders = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_day2\\data\\raw\\orders.csv"
    path_products = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_day2\\data\\raw\\products.csv"
    path_customers = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_day2\\data\\raw\\customers.csv"

    orders = load_csv(path_orders)
    products = load_csv(path_products)
    customers = load_csv(path_customers)

    print("Fichiers chargés avec succès")
    print(f"Orders: {orders.shape}")
    print(f"Products: {products.shape}")
    print(f"Customers: {customers.shape}")


if __name__ == "__main__":
    main()

# %%
