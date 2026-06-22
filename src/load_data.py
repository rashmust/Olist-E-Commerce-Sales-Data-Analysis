import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("olist.db")

data_path = "data/raw"

files = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "products": "olist_products_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv"
}

for table, file in files.items():

    full_path = os.path.join(data_path, file)

    print("Loading:", full_path)

    df = pd.read_csv(full_path)

    df.to_sql(table, conn, if_exists="replace", index=False)

    print(f"{table} loaded → {df.shape}")

conn.close()

print("database created")