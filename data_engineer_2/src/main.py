# -*- coding: utf-8 -*-
#%% Utiser la fonction "load_csv" de ingestion.py pour charger les fichiers CSV
from pathlib import Path
from ingestion import load_csv
from validation import validate_orders, validate_products, validate_customers
from enrichment import enrich_sales  
from golden import save_dataframe     # si tu as une fonction dédiée
from logger import setup_logger
#%% Fonction principale
def run_pipeline(project_root: Path) -> Path:
    """
    Lance le pipeline et retourne le chemin du fichier output.
    """
    logger = setup_logger()
    logger.info("START pipeline")

    raw_dir = project_root / "data" / "raw"
    processed_dir = project_root / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    orders = load_csv(raw_dir / "orders.csv")
    products = load_csv(raw_dir / "products.csv")
    customers = load_csv(raw_dir / "customers.csv")

    orders = validate_orders(orders)
    products = validate_products(products)
    customers = validate_customers(customers)

    sales = enrich_sales(orders, products, customers)

    output_path = processed_dir / "new_golden.parquet"
    sales.to_parquet(output_path, index=False)

    logger.info(f"END pipeline | output={output_path}")
    return output_path

if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    run_pipeline(project_root)

# %%
