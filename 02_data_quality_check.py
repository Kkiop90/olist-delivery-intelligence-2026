import pandas as pd
from pathlib import Path as path 
BASE_DIR = path(__file__).resolve().parent.parent

# Locate raw data
DATA_PATH = BASE_DIR / "data" / "raw"

datapath = path("data/raw")

files =["olist_customers_dataset.csv",
        "olist_geolocation_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_order_payments_dataset.csv",
        "olist_order_reviews_dataset.csv",
        "olist_orders_dataset.csv",
        "olist_products_dataset.csv",
        "olist_sellers_dataset.csv",
        "product_category_name_translation.csv"
        ]
data = {}
for filename in files:
    data[filename]= pd.read_csv(datapath/filename)
    print("n/"+"="*50)# making partiction between datasets
    print("missing values:")
    print(data[filename].isnull().sum())
    print("Duplicated values:")
    print(data[filename].duplicated().sum())
    print("data types:")
    print(data[filename].dtypes)