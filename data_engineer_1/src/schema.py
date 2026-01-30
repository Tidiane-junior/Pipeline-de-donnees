# %% Définition du schéma de la base de données
'''
    On crée explicitement les schémas.
    Jamais de tables implicites en entreprise.
'''
# %% Fonction de creation de schemas des tables de dimensions et de faites
def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_sales (
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price REAL,
            revenue REAL,
            FOREIGN KEY(product_id) REFERENCES dim_product(product_id)
        )
    """)
