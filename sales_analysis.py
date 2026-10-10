# Sales Data Analysis
# Analyzing sales data using Pandas, NumPy, and Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==============================
# LOAD AND INSPECT DATA
# ==============================

# Load the sales data
df = pd.read_csv("data/sales_data.csv")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Calculate sales for each order
df["Sales"] = df["Quantity"] * df["Price"]


print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())

print("\nSales column:")
print(df[["Product", "Quantity", "Price", "Sales"]].head())


# ==============================
# BASIC SALES ANALYSIS
# ==============================

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nAverage Order Value:")
print(df["Sales"].mean())


# ==============================
# PRODUCT ANALYSIS
# ==============================

# Calculate sales by product
product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Find the top-selling product
top_product = product_sales.idxmax()
top_product_sales = product_sales.max()

print("\nTop-Selling Product:")
print(top_product)
print("Total Sales:", top_product_sales)


# ==============================
# CATEGORY ANALYSIS
# ==============================

# Calculate sales by category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# Find the top-selling category
top_category = category_sales.idxmax()
top_category_sales = category_sales.max()

print("\nTop-Selling Category:")
print(top_category)
print("Total Sales:", top_category_sales)


# ==============================
# REGIONAL ANALYSIS
# ==============================

# Calculate sales by region
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

# Find the top-selling region
top_region = region_sales.idxmax()
top_region_sales = region_sales.max()

print("\nTop-Selling Region:")
print(top_region)
print("Total Sales:", top_region_sales)


# ==============================
# MONTHLY ANALYSIS
# ==============================

# Calculate monthly sales
monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Find the best sales month
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print("\nBest Sales Month:")
print(best_month)
print("Total Sales:", best_month_sales)


# ==============================
# STATISTICAL ANALYSIS
# ==============================

# Calculate sales standard deviation
sales_std = np.std(df["Sales"])

print("\nSales Standard Deviation:")
print(sales_std)

# Find high-value orders
high_value_orders = df[df["Sales"] > 10000]

print("\nHigh-Value Orders:")
print(high_value_orders)

# Sort high-value orders by sales
high_value_orders = high_value_orders.sort_values(
    by="Sales",
    ascending=False
)

print("\nHigh-Value Orders Sorted by Sales:")
print(high_value_orders)

# Find the top 5 highest-value orders
top_5_orders = high_value_orders.head(5)

print("\nTop 5 Highest-Value Orders:")
print(top_5_orders)

# Find the 5 lowest-value orders
lowest_5_orders = df.sort_values(
    by="Sales",
    ascending=True
).head(5)

print("\n5 Lowest-Value Orders:")
print(lowest_5_orders)

# Filter Electronics orders
electronics_sales = df[df["Category"] == "Electronics"]

print("\nElectronics Orders:")
print(electronics_sales)

# Calculate total Electronics sales
electronics_total_sales = electronics_sales["Sales"].sum()

print("\nTotal Electronics Sales:")
print(electronics_total_sales)

# Calculate average Electronics order value
electronics_average_order = electronics_sales["Sales"].mean()

print("\nAverage Electronics Order Value:")
print(electronics_average_order)

# Find high-value Electronics orders
high_value_electronics = df[
    (df["Category"] == "Electronics") &
    (df["Sales"] > 10000)
]

print("\nHigh-Value Electronics Orders:")
print(high_value_electronics)

# Find Electronics or Furniture orders
electronics_or_furniture = df[
    (df["Category"] == "Electronics") |
    (df["Category"] == "Furniture")
]

print("\nElectronics or Furniture Orders:")
print(electronics_or_furniture)

# Filter selected categories using isin()
selected_categories = df[
    df["Category"].isin(["Electronics", "Furniture"])
]

print("\nSelected Categories:")
print(selected_categories)

# Sort all orders by sales
sales_sorted = df.sort_values(
    by="Sales",
    ascending=False
)

print("\nAll Orders Sorted by Sales:")
print(sales_sorted)

# Find the top 10 highest-value orders
top_10_orders = sales_sorted.head(10)

print("\nTop 10 Highest-Value Orders:")
print(top_10_orders)

# Calculate total quantity sold by product
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\nTotal Quantity Sold by Product:")
print(product_quantity)

# Find the most-sold product by quantity
most_sold_product = product_quantity.idxmax()
most_sold_quantity = product_quantity.max()

print("\nMost-Sold Product by Quantity:")
print(most_sold_product)
print("Total Quantity Sold:", most_sold_quantity)

# Calculate average price by product
average_price_by_product = df.groupby("Product")["Price"].mean()

print("\nAverage Price by Product:")
print(average_price_by_product)

# Create a complete product summary
product_summary = df.groupby("Product").agg(
    Total_Sales=("Sales", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Average_Price=("Price", "mean")
)

print("\nProduct Summary:")
print(product_summary)

# Find the best-selling product by revenue
best_product = product_summary["Total_Sales"].idxmax()
best_product_sales = product_summary["Total_Sales"].max()

print("\nBest-Selling Product by Revenue:")
print(best_product)
print("Total Sales:", best_product_sales)

# Find the product with the highest quantity sold
most_sold_product = product_summary["Total_Quantity"].idxmax()
most_sold_quantity = product_summary["Total_Quantity"].max()

print("\nProduct with Highest Quantity Sold:")
print(most_sold_product)
print("Total Quantity Sold:", most_sold_quantity)

# Calculate sales contribution percentage by product
product_summary["Sales_Percentage"] = (
    product_summary["Total_Sales"] / df["Sales"].sum()
) * 100

print("\nProduct Sales Contribution:")
print(product_summary)

# Create a complete category summary
category_summary = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Average_Price=("Price", "mean")
)

print("\nCategory Summary:")
print(category_summary)

# Find the best-selling category by revenue
best_category = category_summary["Total_Sales"].idxmax()
best_category_sales = category_summary["Total_Sales"].max()

print("\nBest-Selling Category by Revenue:")
print(best_category)
print("Total Sales:", best_category_sales)

# Find the category with the highest quantity sold
most_sold_category = category_summary["Total_Quantity"].idxmax()
most_sold_category_quantity = category_summary["Total_Quantity"].max()

print("\nCategory with Highest Quantity Sold:")
print(most_sold_category)
print("Total Quantity Sold:", most_sold_category_quantity)

# Calculate sales contribution percentage by category
category_summary["Sales_Percentage"] = (
    category_summary["Total_Sales"] / df["Sales"].sum()
) * 100

print("\nCategory Sales Contribution:")
print(category_summary)

# ==============================
# DATA VISUALIZATION
# ==============================

# Plot monthly sales trend
monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(8, 5)
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.savefig("charts/monthly_sales.png")
plt.show()


# Plot sales by category
category_sales.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)

plt.savefig("charts/sales_by_category.png")
plt.show()


# Plot sales by region
region_sales.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)

plt.savefig("charts/sales_by_region.png")
plt.show()


# Plot sales by product
product_sales.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.savefig("charts/sales_by_product.png")
plt.show()


# ==============================
# FINAL SUMMARY
# ==============================

print("\n========== SALES SUMMARY ==========")

print("Total Sales:", df["Sales"].sum())
print("Average Order Value:", df["Sales"].mean())
print("Top-Selling Product:", top_product)
print("Top-Selling Category:", top_category)
print("Top-Selling Region:", top_region)
print("Best Sales Month:", best_month)
print("Sales Standard Deviation:", sales_std)