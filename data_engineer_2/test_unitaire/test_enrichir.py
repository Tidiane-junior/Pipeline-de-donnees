import pandas as pd
from enrichment import enrich_sales

# tester les 
def test_enrich_sales_computes_revenue():
    orders = pd.DataFrame({
        "order_id": ["order_1"],
        "order_date": ["2024-01-01"],
        "customer_id": ["customer_1"],
        "product_id": ["product_1"],
        "quantity": [2],
        "unit_price": [50.0],
    })

    products = pd.DataFrame({
        "product_id": ["product_1"],
        "product_name": ["Laptop"],
        "category": ["Electronics"],
        "weight_kg": [2.5],
        "price": [1000.0],
    })

    # Données clients fictives pour le test
    customers = pd.DataFrame({
        "customer_id": ["customer_1"],
        "customer_name": ["John Doe"],
        "country": ["FRANCE"],
        "signup_date": ["2023-01-01"],
    })

    df = enrich_sales(orders, products, customers)

    assert "revenue" in df.columns
    assert df.iloc[0]["revenue"] == 100.0
