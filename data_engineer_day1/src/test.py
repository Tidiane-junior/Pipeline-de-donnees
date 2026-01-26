# #%%
# from pathlib import Path
# from utils import setup_logger
# from loader import load_csv
# from processor import validate_data, compute_revenue

# def main():
#     logger = setup_logger()
#     logger.info("Démarrage du pipeline")

#     # Racine du projet (indépendant du point de lancement)
#     project_root = Path(__file__).resolve().parent.parent
#     input_path = project_root / "data" / "raw_sales.csv"

#     try:
#         df = load_csv(input_path)
#         logger.info(f"Fichier chargé avec succès ({len(df)} lignes)")

#         df = validate_data(df)
#         logger.info("Validation des données OK")

#         df = compute_revenue(df)
#         logger.info(f"Chiffre d'affaires total : {df['revenue'].sum()}")

#     except Exception as e:
#         logger.error(f"Erreur dans le pipeline : {e}")
#         raise

#     logger.info("Pipeline terminé avec succès")

# if __name__ == "__main__":
#     main()


# # %%
# import os

# print("Current Working Directory:", os.getcwd())
#%%
import pandas as pd

#%% Charger le fichier CSV
path = "D:\\Data_Engineer_Bootcamp\\data_engineer_day1\\data\\raw_sales.csv"
df = pd.read_csv(path)
df.head(10)
# %%
