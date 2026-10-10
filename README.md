# 📊 Sales Data Analysis & Intelligence Dashboard

A Python-based sales data analysis project that uses **Pandas, NumPy, Matplotlib, and Streamlit** to analyze sales performance and present business insights through an interactive dashboard.

## 📌 Project Overview

This project analyzes a sample sales dataset to understand performance across products, categories, regions, and months.

It includes two components:

- **Sales Analysis Script (`sales_analysis.py`)** — performs data analysis, calculates key sales metrics, and generates visualizations.
- **Interactive Dashboard (`dashboard.py`)** — provides interactive filters, charts, KPIs, business insights, data quality checks, and downloadable reports.

## 🚀 Features

### 📈 Sales Analysis

- Load and inspect sales data from a CSV file.
- Convert order dates into datetime format.
- Calculate sales for each order using quantity and price.
- Calculate total sales and average order value.
- Analyze sales by product, category, region, and month.
- Identify top-performing products, categories, and regions.
- Identify the best sales month.
- Calculate sales standard deviation using NumPy.
- Generate and save visualizations using Matplotlib.

### 📊 Interactive Streamlit Dashboard

- **Sales Overview:** KPI cards, monthly sales trends, sales growth, and performance charts.
- **Interactive Filters:** Filter sales by category, region, and date range.
- **Sales Explorer:** Search for products and view matching orders, revenue, and quantity sold.
- **Ask the Data:** Answer predefined questions about products, categories, regions, and sales performance.
- **Business Recommendations:** Highlight top-revenue products and products with the highest demand.
- **Data Quality:** Check for missing values and duplicate rows.
- **Revenue Contribution:** View product-wise revenue and percentage contribution.
- **Downloadable Reports:** Export filtered sales data and product performance reports as CSV files.
- **Quantity vs Revenue Analysis:** Compare product quantities with their generated revenue.
- **Dataset Information:** View the number of filtered records and the selected date range.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Git and GitHub

## 📂 Project Structure

```text
Sales_Data_Analysis/
│
├── charts/
│   ├── monthly_sales.png
│   ├── sales_by_category.png
│   ├── sales_by_region.png
│   └── sales_by_product.png
│
├── data/
│   └── sales_data.csv
│
├── dashboard.py
├── sales_analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/RiyaGirdhar30/Sales-Data-Analysis.git
```

### 2. Navigate to the project directory

```bash
cd Sales-Data-Analysis
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the sales analysis script

```bash
python sales_analysis.py
```

The script performs the sales analysis and generates visualizations in the `charts/` directory.

### 5. Launch the interactive dashboard

```bash
python -m streamlit run dashboard.py
```

Streamlit will provide a local URL that you can open in your browser to explore the dashboard.

## 📊 Visualizations

The project includes visualizations for:

- Monthly sales trends
- Sales by category
- Sales by region
- Sales by product
- Monthly sales growth
- Quantity versus revenue relationships

The standalone analysis script generates Matplotlib charts, while the dashboard displays interactive charts based on the selected filters.

## 📁 Dataset

The dataset is stored at:

```text
data/sales_data.csv
```

It contains the following columns:

- `Order Date`
- `Product`
- `Category`
- `Region`
- `Quantity`
- `Price`

Sales for each order are calculated using:

```text
Sales = Quantity × Price
```

The dashboard derives its results from this dataset. Its metrics and visualizations update according to the selected filters.

## 🔮 Future Improvements

- Add larger and more realistic sales datasets.
- Expand statistical analysis and business insights.
- Improve chart customization and dashboard responsiveness.
- Add additional analytical questions and reporting options.
- Deploy the Streamlit dashboard for public access.

## 👩‍💻 Author

**Riya Girdhar**

- GitHub: [RiyaGirdhar30](https://github.com/RiyaGirdhar30)
- LinkedIn: [Riya Girdhar](https://www.linkedin.com/in/riya-girdhar-a6074124a)