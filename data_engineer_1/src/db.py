# %% Mise en place de la base (SQLite)
import sqlite3
from pathlib import Path

# Fonction pour obtenir une connexion à la base de données
def get_connection(db_path: Path):
    """
    Crée une connexion à la base SQLite.
    """
    # Assurer que le répertoire de la base de données existe
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)
