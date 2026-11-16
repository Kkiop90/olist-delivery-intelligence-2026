import pandas as pd  
from pathlib import Path

# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Locate the raw data folder
DATA_PATH = BASE_DIR / "data" / "raw"

# Load orders dataset
orders = pd.read_csv(DATA_PATH / "olist_orders_dataset.csv")
reviews = pd.read_csv(DATA_PATH / "olist_order_reviews_dataset.csv")
print(orders.head())
#review_id                    str
#order_id                     str
#review_score               int64
#review_comment_title         str
#review_comment_message       str
#review_creation_date         str
#review_answer_timestamp      str
#dtype: object
print(reviews.head())
print(orders.columns)
print(reviews.columns)
#Index(['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp',
 #     'order_delivered_customer_date', 'order_estimated_delivery_date'],
  #    dtype='str')
#Index(['review_id', 'order_id', 'review_score', 'review_comment_title',
   #    'review_comment_message', 'review_creation_date',
    #   'review_answer_timestamp'],
     # dtype='str')
#for finding row and columns
print(orders.shape)
print(reviews.shape)
#converting to time and date format h:m:s,y:m:d by pd.to_datetime
orders['order_purchase_timestamp']=pd.to_datetime(orders['order_purchase_timestamp'], format='%Y-%m-%d %H:%M:%S')
orders['order_estimated_delivery_date']=pd.to_datetime(orders['order_estimated_delivery_date'], format='%Y-%m-%d %H:%M:%S')
orders['order_delivered_customer_date']=pd.to_datetime(orders['order_delivered_customer_date'], format='%Y-%m-%d %H:%M:%S')
orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"], errors="coerce"
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"], errors="coerce"
)
#finding delays in delivery
delivery_delay = (
    orders["order_delivered_customer_date"]
    - orders["order_estimated_delivery_date"]
)

orders["delivery_delay_days"] = delivery_delay.dt.days

print("Delivery Delay (Days):", orders["delivery_delay_days"].head(10))

orders[["order_id", "delivery_delay_days"]]
reviews[["order_id", "review_score"]]
print(orders)
print(reviews)

delivery_data = orders[["order_id", "delivery_delay_days"]]
reviews_data = reviews[["order_id", "review_score"]]
delivery_reviews=delivery_data.merge(reviews_data, on="order_id")
print(delivery_reviews)
print(delivery_reviews.shape)
#finding only the value that is not not null and by sum into full number
print(delivery_reviews.notna().sum())

valid_delivery_review = delivery_reviews[
    delivery_reviews["delivery_delay_days"].notna()
].copy()
print("valid_delivery_review:",valid_delivery_review)
print(valid_delivery_review.shape)
#average customer rating per order
order_reviews = reviews.groupby("order_id").agg(
    average_rating=("review_score", "mean"),
    review_count=("review_score", "count")
).reset_index()
print("Average customer rating per order:",order_reviews.head())
print(order_reviews.shape)
final_data = delivery_data.merge(
    order_reviews[["order_id", "average_rating", "review_count"]],
    on="order_id",
    how="left"
)
print(final_data.head())
final_data = final_data.dropna(subset=["delivery_delay_days"]).copy()
final_data["delivery_category"] = final_data["delivery_delay_days"].gt(0).map({
    True: "late",
    False: "Early/on time",
})

#Compare average customer ratings by delivery category
rating_comparison = final_data.groupby("delivery_category").agg(
    total_orders=("order_id", "count"),
    average_rating=("average_rating", "mean")
).reset_index()

print(rating_comparison)

final_data = final_data[
    ["order_id", "delivery_delay_days", "delivery_category",
     "average_rating", "review_count"]
]
print(final_data)
PROCESSED_PATH = BASE_DIR / "data" / "processed"
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
output_file = PROCESSED_PATH / "delivery_satisfaction_analysis.csv"

final_data.to_csv(output_file, index=False)
print("Final dataset saved successfully:", output_file)