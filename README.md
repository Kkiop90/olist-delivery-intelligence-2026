# olist-delivery-intelligence-2026
# Olist Delivery Intelligence Dashboard
### Delivery Performance & Customer Satisfaction Analysis

## 1. Project Overview

This is an independent Data Analytics project using the Brazilian E-Commerce Public Dataset by Olist.

The project analyses e-commerce delivery performance and its relationship with customer satisfaction.

The main objective is to transform raw e-commerce data into meaningful business insights using Python, Pandas and Power BI.

**Project Workflow:**

Raw Data → ETL → Processed Data → EDA → Power BI Dashboard → Business Insights

## 2. Business Questions

This project investigates the following business questions:

1. What percentage of orders were delivered late?
2. How many orders were delivered early or on time?
3. How are delivery delays distributed?
4. Do late deliveries receive lower customer ratings?
5. What is the average customer rating for late versus early/on-time deliveries?
6. How can delivery performance improvements support customer satisfaction?

## 3. Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| Power BI | Interactive dashboard |
| Git & GitHub | Version control and project hosting |

## 4. Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist  
**Source:** Kaggle

The project contains nine original CSV datasets.

### Raw Data

Stored in `Data/raw/`:

- olist_customers_dataset.csv
- olist_geolocation_dataset.csv
- olist_order_items_dataset.csv
- olist_order_payments_dataset.csv
- olist_order_reviews_dataset.csv
- olist_orders_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv
- product_category_name_translation.csv

These files represent the original source data.

### Processed Data

Stored in `Data/processed/`:

`delivery_satisfaction_analysis.csv`

The processed dataset contains:

- order_id
- delivery_delay_days
- delivery_category
- average_rating
- review_count

## 5. ETL – Extract, Transform & Load

### Extract
- Loaded original Olist CSV files using Pandas.
- Inspected dataset shapes, columns and data types.

### Transform
- Checked missing values and duplicate records.
- Converted delivery date columns into datetime format.
- Calculated delivery delay in days.
- Grouped customer reviews by order.
- Calculated average customer ratings and review counts.
- Merged delivery information with customer review information.
- Created delivery categories: Late and Early/On-Time.

### Load
- Exported the prepared dataset into CSV format.
- Saved the output in `Data/processed/`.
- Imported the processed dataset into Power BI.

## 6. EDA – Exploratory Data Analysis

Exploratory Data Analysis was performed to identify patterns and understand business performance.

### Customer Analysis
- Unique customer analysis.
- Repeat customer behaviour.

### Order & Delivery Analysis
- Order status distribution.
- Delivered and cancelled orders.
- Delivery delay calculations.
- Late versus early/on-time delivery analysis.
- Identification of highly delayed orders.

### Customer Satisfaction Analysis
- Customer review score distribution.
- Average customer ratings.
- Satisfied, neutral and dissatisfied customer groups.
- Comparison of ratings between late and early/on-time deliveries.

## 7. Key Findings

Based on the Python analysis:

| Metric | Result |
|---|---:|
| Analysed delivery records | 96,476 |
| Late deliveries | 6,535 |
| Late delivery rate | 6.77% |
| Early/on-time deliveries | 89,941 |
| Early/on-time delivery rate | 93.23% |
| Average rating – Early/On-Time | 4.29 / 5 |
| Average rating – Late | 2.27 / 5 |

### Business Insight

Late deliveries have a significantly lower average customer rating compared with early/on-time deliveries.

The analysis indicates a strong association between delivery delays and lower customer satisfaction. However, it does not establish that delivery delays alone cause lower ratings.

## 8. Power BI Dashboard

The interactive dashboard includes:

- Total Orders
- Average Customer Rating
- Late Delivery Rate
- Early/On-Time vs Late Orders
- Delivery Delay Distribution
- Average Rating by Delivery Category
- Delivery Delay vs Average Customer Rating

## 9. Project Structure

```text
olist_delivery_intelligence/
│
├── .vscode/
│
├── Data/
│   ├── raw/
│   │   └── Original Olist CSV files
│   │
│   └── processed/
│       └── delivery_satisfaction_analysis.csv
│
├── Notebooks/
│   ├── 01_load_all_datasets.py
│   ├── 02_data_quality_check.py
│   ├── 03_customer_analysis.py
│   ├── 04_orders_analysis.py
│   └── 05_delivery_vs_satisfaction.py
│
├── PowerBI/
│   └── olist_dashboard.pbix
│
├── Reports/
│   └── dashboard_screenshot.png
│
├── src/
│   └── data_loader.py
│
└── README.md
```

## 10. Python Script Description

| Script | Purpose |
|---|---|
| 01_load_all_datasets.py | Loading and inspecting datasets |
| 02_data_quality_check.py | Data quality checks |
| 03_customer_analysis.py | Customer analysis and EDA |
| 04_orders_analysis.py | Order and delivery analysis |
| 05_delivery_vs_satisfaction.py | Delivery and satisfaction analysis, transformation and export |

## 11. Skills Demonstrated

- ETL (Extract, Transform, Load)
- Exploratory Data Analysis (EDA)
- Data Cleaning and Preprocessing
- Python Programming
- Pandas
- Data Merging and Aggregation
- Business Analysis
- Power BI Dashboard Development
- Data Visualisation
- Business Insight Generation

## 12. Conclusion

This project demonstrates an end-to-end data analytics workflow using real-world e-commerce data.

By combining delivery performance information with customer reviews, the analysis identifies an important relationship between delivery delays and customer satisfaction.

The findings can help businesses understand delivery performance and identify areas that may require operational improvement.

---

**Project Type:** Independent Data Analytics Project  
**Domain:** E-Commerce / Business Analytics  
**Author:** Krish Keshari  
**Technologies:** Python, Pandas, Power BI
