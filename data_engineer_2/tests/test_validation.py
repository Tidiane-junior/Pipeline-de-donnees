import pandas as pd
from validation import validate_orders


def test_validate_orders_filters_invalid_rows():
    df = pd.DataFrame({
        "order_id": ["order_1", None],
        "order_date": ["2024-01-01", "2024-01-02"],
        "customer_id": ["customer_2", "customer_3"],
        "product_id": ["product_1", "product_2"],
        "quantity": [1, -5],
        "unit_price": [10.0, 20.0],
    })

    clean_df = validate_orders(df)

    assert clean_df.shape[0] == 1
    assert clean_df.iloc[0]["quantity"] > 0
