import pandas as pd
from ingestion import load_csv
import tempfile

# Fonction de test pour la fonction load_csv
def test_load_csv_success():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        # sauvegarder des données CSV temporaires
        f.write("col1,col2\n1,2\n3,4") 

    df = load_csv(f.name)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)

# Fonction de test pour la gestion des erreurs lorsque le fichier n'existe pas
def test_load_csv_file_not_found():
    try:
        load_csv("fichier_inexistant.csv")
        assert False
    except FileNotFoundError:
        assert True
