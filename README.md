# 🏗️ Data Engineer : Mise en place d'un pipeline complet

## 🎯 Objectif

Construire un **pipeline data complet et structuré**, permettant de transformer des données brutes e-commerce en un dataset analytique exploitable.

Je suis en **mission de consultant Data Engineer** : ingestion, validation, enrichissement.

---

## 🧠 Cas métier

Nous travaillons sur un cas **e-commerce** avec :

* des commandes clients
* un référentiel produits
* un référentiel clients

L’objectif est de produire une table finale de ventes enrichies, prête pour :

* la BI
* un data warehouse
* des analyses business

---

## 📁 Structure du projet

```
data_engineer_day3/
├── src/
│   ├── main.py          # Orchestration du pipeline
│   ├── ingestion.py    # Chargement des données brutes
│   ├── validation.py   # Règles de qualité et validation
│   └── enrichment.py  # Jointures et calculs business
│
├── data/
│   ├── raw/            # Données brutes (non modifiées)
│   │   ├── orders.csv
│   │   ├── products.csv
│   │   └── customers.csv
│   └── processed/      # Données transformées (étape suivante)
│
└── README.md
```

👉 **Règle Data Engineer** : le dossier `raw/` est immuable.

---

## 🗂️ Schéma des données

### 📦 orders.csv (table de faits)

| Colonne     | Description          |
| ----------- | -------------------- |
| order_id    | Identifiant commande |
| order_date  | Date de commande     |
| customer_id | Identifiant client   |
| product_id  | Identifiant produit  |
| quantity    | Quantité             |
| unit_price  | Prix unitaire        |

### 🛍️ products.csv (dimension produit)

| Colonne      | Description         |
| ------------ | ------------------- |
| product_id   | Identifiant produit |
| product_name | Nom                 |
| category     | Catégorie           |
| weight_kg    | Poids               |
| price        | Prix catalogue      |

### 👤 customers.csv (dimension client)

| Colonne       | Description        |
| ------------- | ------------------ |
| customer_id   | Identifiant client |
| customer_name | Nom                |
| country       | Pays               |
| signup_date   | Date d’inscription |

---

## 🔄 Étapes du pipeline

### 1️⃣ Ingestion (`ingestion.py`)

* Chargement des fichiers CSV depuis `data/raw/`
* Vérification de l’existence des fichiers
* Aucune transformation appliquée

### 2️⃣ Validation (`validation.py`)

* Vérification du schéma attendu
* Suppression des valeurs invalides
* Application des règles métier (quantité, prix, unicité)

### 3️⃣ Enrichissement (`enrichment.py`)

* Jointure orders ↔ products ↔ customers
* Calcul du chiffre d’affaires (`revenue`)
* Sélection des colonnes utiles

### 4️⃣ Golden layer (golden.py)

* Écriture des données propres dans data/processed/
* Création automatique des dossiers
* Dataset prêt pour BI / Warehouse

### 5️⃣ Logs structurés (logger.py)

* Logger centralisé pour le pipeline
* Logs fichier + console
* Horodatage, niveaux de logs, traçabilité complète
* Gestion des erreurs avec stacktrace

---

## ▶️ Exécution du pipeline

Depuis la racine du projet :

```bash
python src/main.py
```

---

## 🧪 Tests unitaires

Le projet inclut une suite de tests unitaires avec pytest afin de sécuriser chaque brique du pipeline.

### Modules testés

  - Ingestion des données (existence des fichiers, chargement CSV)
  - Validation des règles métier
  - Enrichissement et calcul du chiffre d’affaires
  - Les tests permettent de :
  - détecter rapidement les régressions
  - fiabiliser le pipeline
  - faciliter le refactoring

L’exécution se fait via :

---
    pytest


## 🧑‍💼 Compétences démontrées

 - Structuration d’un projet data
 - Séparation des responsabilités
 - Qualité et fiabilité des données
 - Mise en place de logs structurés
 - Tests unitaires avec pytest
 - Bases solides du métier de Data Engineer / Consultant data



---

🚀 *Projet réalisé dans une logique entreprise, orientée production et passage à l’échelle.*
