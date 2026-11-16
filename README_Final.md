# Olist Delivery Intelligence Dashboard
### Delivery Performance & Customer Satisfaction Analysis

## Project Overview
This independent data analytics project uses the Brazilian E-Commerce Public Dataset by Olist to explore delivery performance and its relationship with customer satisfaction.

The project demonstrates an end-to-end analytics workflow:
- **ETL:** Extracting, checking, transforming and loading data.
- **EDA:** Exploring the data to identify patterns and answer business questions.
- **Power BI:** Presenting key metrics and findings in an interactive dashboard.

## Tools Used
- Python
- Pandas
- Power BI
- Git and GitHub

## Dataset
**Source:** Brazilian E-Commerce Public Dataset by Olist (Kaggle).

### Raw data
The `Data/raw/` folder contains the original source CSV files:
- `olist_customers_dataset.csv`
- `olist_geolocation_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`
- `product_category_name_translation.csv`

These are source files. They should remain unchanged so the analysis can be reproduced from the original data.

### Processed data
The `Data/processed/` folder contains the prepared output:
- `delivery_satisfaction_analysis.csv`

This processed file combines order delivery-delay information with order-level customer review information. It includes:
- `order_id`
- `delivery_delay_days`
- `delivery_category`
- `average_rating`
- `review_count`

## ETL Process

### 1. Extract
- Load the original Olist CSV files from `Data/raw/` using Pandas.
- Inspect dataset shapes, columns and data types.

### 2. Transform
- Check missing values and duplicate records.
- Convert delivery date fields to datetime.
- Calculate delivery delay by comparing actual delivery date with estimated delivery date.
- Group review records by order and calculate average rating and review count.
- Merge delivery information with order-level review information.
- Create a delivery category: `late` or `Early/on time`.

### 3. Load
- Export the prepared analysis data to `Data/processed/delivery_satisfaction_analysis.csv`.
- Import the processed CSV into Power BI.

## EDA – Exploratory Data Analysis

The analysis scripts explore:

### Customer Analysis
- Unique customer counts.
- Repeat customer behaviour.

### Order and Delivery Analysis
- Order status distribution.
- Delivered, cancelled and other order statuses.
- Delivery delay in days.
- Late versus early/on-time counts and rates.
- Most delayed orders.

### Customer Satisfaction Analysis
- Review score distribution and average rating.
- Dissatisfied, neutral and satisfied review groups.
- Average rating for late versus early/on-time deliveries.

## Business Questions
1. What proportion of analysed orders were delivered late?
2. How are delivery delays distributed?
3. What is the average customer rating for late deliveries compared with early/on-time deliveries?
4. Is delivery delay associated with customer satisfaction?

## Key Findings
Based on the current Python analysis:

| Metric | Result |
|---|---:|
| Orders with valid delivery-delay records | 96,476 |
| Late deliveries | 6,535 |
| Late delivery rate | 6.77% |
| Early/on-time deliveries | 89,941 |
| Early/on-time delivery rate | 93.23% |
| Average rating for early/on-time deliveries | 4.29 / 5 |
| Average rating for late deliveries | 2.27 / 5 |

Late deliveries have a substantially lower average rating than early/on-time deliveries. This indicates an association between delivery delays and lower customer ratings; it does not prove that delays alone cause lower ratings.

## Power BI Dashboard
The dashboard includes:
- Total analysed orders
- Average customer rating
- Late delivery rate
- Early/on-time versus late delivery split
- Delivery delay distribution
- Average rating by delivery category
- Delivery delay versus average customer rating

Place a screenshot of the finished dashboard in `Reports/`, then add this image reference (update the filename if necessary):

`![Olist Delivery Intelligence Dashboard](Reports/dashboard_screenshot.png)`

## Project Structure

```text
olist_delivery_intelligence/
|
|-- .vscode/
|
|-- Data/
|   |-- raw/
|   |   |-- olist_customers_dataset.csv
|   |   |-- olist_geolocation_dataset.csv
|   |   |-- olist_order_items_dataset.csv
|   |   |-- olist_order_payments_dataset.csv
|   |   |-- olist_order_reviews_dataset.csv
|   |   |-- olist_orders_dataset.csv
|   |   |-- olist_products_dataset.csv
|   |   |-- olist_sellers_dataset.csv
|   |   `-- product_category_name_translation.csv
|   |
|   `-- processed/
|       `-- delivery_satisfaction_analysis.csv
|
|-- Notebooks/
|   |-- 01_load_all_datasets.py
|   |-- 02_data_quality_check.py
|   |-- 03_customer_analysis.py
|   |-- 04_orders_analysis.py
|   `-- 05_delivery_vs_satisfaction.py
|
|-- PowerBI/
|   `-- olist_dashboard.pbix
|
|-- Reports/
|   `-- dashboard_screenshot.png
|    --c:\Users\krish\OneDrive\Desktop\olist_delivery_intelligence\Reports\# Olist Project – Customer Repeat P.txt            --c:\Users\krish\OneDrive\Desktop\olist_delivery_intelligence\Reports\# Olist Project – Data Quality Chec.txt --c:\Users\krish\OneDrive\Desktop\olist_delivery_intelligence\Reports\# Olist Project – Order, Delivery Performance part 4.txt --c:\Users\krish\OneDrive\Desktop\olist_delivery_intelligence\Reports\Olist Project – Delivery Performanc.txt --c:\Users\krish\OneDrive\Desktop\olist_delivery_intelligence\Reports\Olist Project – Python Data Loadi.txt
|
|-- src/
|   `-- data_loader.py
|
`-- README.md
```

Folder and file names in the tree are based on the project structure shared so far. Keep the actual spelling and capitalisation used on your computer, or rename folders consistently and update any file paths in your Python scripts.

## Script Guide: ETL and EDA

| Script | Main role |
|---|---|
| `01_load_all_datasets.py` | Extracts and loads source CSV files for inspection |
| `02_data_quality_check.py` | Checks data quality, missing values and duplicates |
| `03_customer_analysis.py` | Explores customer and repeat-purchase patterns (EDA) |
| `04_orders_analysis.py` | Explores order status and delivery performance (EDA) |
| `05_delivery_vs_satisfaction.py` | Prepares/merges delivery and review data, calculates comparisons and exports the processed CSV (ETL + EDA) |

This mapping reflects the scripts' intended roles. The exact operations should be confirmed against each script's code.

## How to Run
1. Install Python.
2. Install Pandas using `pip install pandas`.
3. Keep original source CSV files in `Data/raw/`.
4. Run the numbered Python scripts from the `Notebooks/` folder, following their order and the file paths configured in the scripts.
5. Open the Power BI report in Power BI Desktop.

## Skills Demonstrated
- ETL fundamentals: extraction, transformation and loading
- Data quality checks
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Pandas data manipulation
- Dataset merging and aggregation
- Business analysis
- Power BI dashboard development
- Communicating data-driven insights

## Project Status
Python analysis and a Power BI dashboard have been created. The README, dashboard screenshot and repository can be refined before publication.

## Author
**Krish Keshari**

Independent Data Analytics Project  
Domain: E-Commerce / Business Analytics  
Tools: Python, Pandas, Power BI
