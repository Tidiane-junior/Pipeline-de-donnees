# %% Importer les modules nécessaires 
from utils import setup_logger
from loader import load_csv, load_csv_in_chunks
from processor import validate_data, compute_revenue

# %% Fonction principale du pipeline
def main():
    logger = setup_logger()
    logger.info("Demarrage du pipeline")

    INPUT_PATH = "D:\\Data_Engineer_Bootcamp\\data_engineer_day1\\data\\raw_sales.csv"

    try:
    # Traitement complet    
        df = load_csv(INPUT_PATH)
        logger.info(f"Fichier bien lu ({len(df)} lignes)")

        df = validate_data(df)
        logger.info("Data validation OK")

        df = compute_revenue(df)
        logger.info("Calcul du chiffre d'affaires ok")

        print(df.head())
    # Traitement par chunks
        # for chunk in load_csv_in_chunks(INPUT_PATH, chunksize=5):
        #     chunk = validate_data(chunk)
        #     chunk = compute_revenue(chunk)
        #     print(chunk.head())

    except Exception as e:
        logger.error(f"Erreur dans le pipeline : {e}")
        raise

    logger.info("Pipeline fini avec succes")

# Exécution de la fonction principale 
if __name__ == "__main__":
    main()




