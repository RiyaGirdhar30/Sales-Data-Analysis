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