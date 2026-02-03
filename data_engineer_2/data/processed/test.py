# %%
import pandas as pd

path = "D:\\Data_Engineer_Bootcamp\\Pipeline-de-donnees\\data_engineer_2\\data\\processed\\golden.parquet"
sales = pd.read_parquet(path)
sales.head()
# %%
