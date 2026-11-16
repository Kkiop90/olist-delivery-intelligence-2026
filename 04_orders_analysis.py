import pandas as pd
from pathlib import Path

# Locate the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Locate raw data
DATA_PATH = BASE_DIR / "data" / "raw"

# Load orders dataset
orders = pd.read_csv(DATA_PATH / "olist_orders_dataset.csv")

print(orders)
print(orders.shape)
print(orders.columns.tolist())
#kpi
print("total orders:")
print(len(orders))
print("canceled orders:")
print(len(orders[orders['order_status']=='canceled']))
print("delivered orders:")
print(len(orders[orders['order_status']=='delivered']))
print("shipped orders:")
print(len(orders[orders['order_status']=='shipped']))
print("order status distribution:")
print(orders['order_status'].value_counts(normalize=True))
canceled_orders_rate= len(orders[orders['order_status']=='canceled'])/len(orders)
print("canceled_orders_rate%:", canceled_orders_rate*100)
non_delivered_orders_rate = len(orders[orders['order_status']!='delivered'])-len(orders[orders['order_status']=='canceled'])
print("non_delivered_orders_rate%:",round( non_delivered_orders_rate*100/len(orders),2))
non_delivered_orders = len(orders[orders['order_status']!='delivered'])-len(orders[orders['order_status']=='canceled'])
print("non_delivered_orders:", non_delivered_orders)



# date-conversion
orders['order_purchase_timestamp']=pd.to_datetime(orders['order_purchase_timestamp'], format='%Y-%m-%d %H:%M:%S')
orders['order_estimated_delivery_date']=pd.to_datetime(orders['order_estimated_delivery_date'], format='%Y-%m-%d %H:%M:%S')
orders['order_delivered_customer_date']=pd.to_datetime(orders['order_delivered_customer_date'], format='%Y-%m-%d %H:%M:%S')
orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"], errors="coerce"
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"], errors="coerce"
)
delivery_delay = (
    orders["order_delivered_customer_date"]
    - orders["order_estimated_delivery_date"]
)

orders["delivery_delay_days"] = delivery_delay.dt.days

print("Delivery Delay (Days):", orders["delivery_delay_days"].head(10))

# late deliveries
late_deliveries = orders[orders['delivery_delay_days']>0]
# ontime deliveries
ontime_deliveries = orders[orders['delivery_delay_days']<=0]
#valid deliveries
valid_delivery = orders[orders['delivery_delay_days'].notnull()]
print("late deliveries:", len(late_deliveries))
print("ontime deliveries:", len(ontime_deliveries))
print("valid deliveries:", len(valid_delivery))
#late_delivery_rate
late_delivery_rate = len(late_deliveries)/len(valid_delivery)*100
print("late_delivery_rate%:", round(late_delivery_rate,2))
#ontime_delivery_rate
ontime_delivery_rate = len(ontime_deliveries)/len(valid_delivery)*100
print("ontime_delivery_rate%:", round(ontime_delivery_rate,2))
#average delivery delay
average_delivery_delay = late_deliveries['delivery_delay_days'].mean()
print("average_delivery_delay:", round(average_delivery_delay,2),"days")
#maxium_delivery_delay
print("maxium_delivery_delay",late_deliveries['delivery_delay_days'].max(),"days")
#minumum_delivery_delay
print("minumum_delivery_delay",late_deliveries['delivery_delay_days'].min(),"days")

# worst_delivery
worst_delivery =late_deliveries.nlargest(5,"delivery_delay_days")
print("worst_delivery",worst_delivery[["order_id","order_status","delivery_delay_days"]])

reviews = pd.read_csv(DATA_PATH / "olist_order_reviews_dataset.csv")

worst_delivery_reviews = worst_delivery.merge(
    reviews[["order_id", "review_score", "review_comment_message"]],
    on="order_id",
    how="left"
)

print(worst_delivery_reviews[[
    "order_id",
    "delivery_delay_days",
    "review_score",
    "review_comment_message"
]])




# continuing the code of analysis with review
data = pd.read_csv(DATA_PATH/"olist_order_reviews_dataset.csv")
print(data.head())
print(data.columns)
print(data.dtypes)
print("customer_rating",data["review_score"].value_counts(),data["review_score"].head(100))
#review_id                    str
#order_id                     str
#review_score               int64
#review_comment_title         str
#review_comment_message       str
#review_creation_date         str
#review_answer_timestamp      str
#dtype: object
avearge_rating = data["review_score"].mean()
print("average customer rating",round(avearge_rating),2,"%")
#coustomer who is not stasisfy
low_customer_rating = data["review_score"]<=2
print("unstatisfy_customer:", low_customer_rating.sum())
#statisfy customer
statisfy_range_customer = data["review_score"]>=3
print("statisfy_customer:", statisfy_range_customer.sum())
# dissatisfy customer rate
print("dissatisfaction rate:")
print(low_customer_rating.sum()/len(data)*100)
# sattisfy customer rate
print("statisfy_customer rate:")
print(statisfy_range_customer.sum()/len(data)*100)
#unique order
print("unique order:-")
print(data["order_id"].nunique())
#repeted ordere
print("repated_orders:")
print(data["order_id"].duplicated().sum())
#order count
order_counts = data["order_id"].value_counts()
print(order_counts[order_counts == 1])
#dupicate ordere count
print(len(order_counts[order_counts >1]))
