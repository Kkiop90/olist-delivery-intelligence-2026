import pandas as pd
from pathlib import Path as path    
datapath = path("data/raw")
customer = pd.read_csv(datapath/"olist_customers_dataset.csv")

print("Total number of customers:")
print(len(customer))
######################################################
# Count how many records belong to each actual customer
customer_counts = customer["customer_unique_id"].value_counts()

# Select customers appearing more than once
repeat_customers = customer_counts[customer_counts > 1]

# Calculate metrics
total_customers = customer["customer_unique_id"].nunique()

number_of_repeat_customers = len(repeat_customers)

records_from_repeat_customers = repeat_customers.sum()

repeat_customer_rate = (
    number_of_repeat_customers / total_customers
) * 100

print("Total actual customers:", total_customers)

print("Number of repeat customers:", number_of_repeat_customers)

print("Records from repeat customers:", records_from_repeat_customers)

print("Repeat customer rate:", round(repeat_customer_rate, 2), "%")

print("\nTop 10 repeat customers:")
print(repeat_customers.head(10))