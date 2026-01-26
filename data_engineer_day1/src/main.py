# %% Importer les modules nécessaires 
from utils import setup_logger
from loader import load_csv, load_csv_in_chunks
from processor import validate_data, compute_revenue

# %% Fonction main version 1 du pipeline 
# def main():
#     logger = setup_logger()
#     logger.info("Demarrage du pipeline")

    # INPUT_PATH = "D:\\Data_Engineer_Bootcamp\\data_engineer_day1\\data\\raw_sales.csv"

#     try:
#     # Traitement complet    
#         # df = load_csv(INPUT_PATH)
#         # logger.info(f"Fichier bien lu ({len(df)} lignes)")

#         # df = validate_data(df)
#         # logger.info("Data validation OK")

#         # df = compute_revenue(df)
#         # logger.info("Calcul du chiffre d'affaires ok")

#         # print(df.head())
#     # Traitement par chunks
#         for chunk in load_csv_in_chunks(INPUT_PATH, chunksize=5):
#             chunk = validate_data(chunk)
#             chunk = compute_revenue(chunk)
#             print(chunk.head())

#     except Exception as e:
#         logger.error(f"Erreur dans le pipeline : {e}")
#         raise

#     logger.info("Pipeline fini avec succes")

# # Exécution de la fonction principale 
# if __name__ == "__main__":
#     main()


# %% Fonction main version 2 du pipeline
from utils import setup_logger, write_parquet
from loader import load_csv_in_chunks
from processor import process_chunk
import pandas as pd

def main():
    logger = setup_logger()
    logger.info("Demarrage du pipeline batch")

    processed_chunks = []
    chemin = "D:\\Data_Engineer_Bootcamp\\data_engineer_day1\\data\\raw_sales.csv"
    
    try:
        for chunk in load_csv_in_chunks(chemin, chunksize=10):
            logger.info(f"Traitement d'un chunk de taille {len(chunk)}")

            processed_chunk = process_chunk(chunk)
            processed_chunks.append(processed_chunk)

        final_df = pd.concat(processed_chunks, ignore_index=True)
        logger.info("Concatenation des chunks terminee")

        write_parquet(final_df, "data/processed/sales.parquet")
        logger.info("Fichier Parquet écrit avec succes")

        print(final_df)

    except Exception as e:
        logger.error(f"Erreur pipeline batch : {e}")
        raise

    logger.info("Pipeline batch termine avec succes")

if __name__ == "__main__":
    main()


# %%
