# -*- coding: utf-8 -*-
#%% Utiser la fonction "load_csv" de ingestion.py pour charger les fichiers CSV
from ingestion import load_csv
from validation import validate_orders, validate_products, validate_customers
from enrichment import enrich_sales
# from data_engineer_2.src.enrichment import enrich_sales
from golden import save_dataframe
from logger import setup_logger
#%% Fonction principale
def main():
    logger = setup_logger()
    logger.info("Le pipeline commence.")

    try:

        # Chemins des fichiers CSV
        path_orders = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_2\\data\\raw\\orders.csv"
        path_products = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_2\\data\\raw\\products.csv"
        path_customers = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_2\\data\\raw\\customers.csv"

        # Chargement des fichiers CSV
        orders = load_csv(path_orders)
        products = load_csv(path_products)
        customers = load_csv(path_customers)

        logger.info(
            f"Table des commandes | orders={orders.shape}")

        logger.info(
            f"Table des produits | products={products.shape}")

        logger.info(
            f"Table des clients | customers={customers.shape}")

        # Validation des données
        orders = validate_orders(orders)
        products = validate_products(products)
        customers = validate_customers(customers)

        logger.info("Data validation well done.")

        # Enrichissement des données
        sales = enrich_sales(orders, products, customers)
        logger.info(f"Data enrichies | sales={sales.shape}")

        save_dataframe(
            sales,
            "data/processed/sales.parquet"
        )

        logger.info("Data well saved as sales.parquet in data/processed.")

    except Exception as e:
        logger.error(f"Erreur dans le pipeline : {e}", exc_info=True)
        raise

    logger.info("Pipeline successfully finished.")

    print(sales.head())

if __name__ == "__main__":
    main()

# %%
