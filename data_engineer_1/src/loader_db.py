# %% Chargement des données dans la base de données
'''
En tant que Data Engineer, j'alimente la base depuis mes pipelines.
'''
#%% Fonctions d'insertion dans la base de données
def insert_products(cursor, products):
    '''
    Insèrer des produits dans la table dim_product.
    cursor : curseur de la base de données
    products : liste de tuples (product_id, product_name)

    '''
    # Utilisation de INSERT OR IGNORE pour éviter les doublons
    cursor.executemany(
        "INSERT OR IGNORE INTO dim_product VALUES (?, ?)",
        products
    )


def insert_sales(cursor, sales):
    cursor.executemany(
        "INSERT INTO fact_sales VALUES (?, ?, ?, ?)",
        sales
    )

# %%
