# Modular Sales Analytics & Reporting System

## Project Overview

The Modular Sales Analytics & Reporting System is a Python-based business intelligence application designed to simulate real-world sales data processing and analytics workflows.  

The system loads raw sales data from CSV/Excel files, performs data cleaning and validation, computes key business metrics, generates visual insights, and exports structured reports through a command-line interface (CLI).

This project demonstrates modular software architecture, clean data engineering practices, and practical business analytics implementation.

---

## Objectives

- Process raw sales datasets efficiently
- Perform structured data cleaning and preprocessing
- Compute key business KPIs
- Analyze category-wise and time-based sales trends
- Generate professional visual reports
- Export automated Excel and executive summary reports
- Maintain modular and scalable architecture

---

## Tech Stack

- **Python**
- **Pandas** – Data manipulation & analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **OpenPyXL** – Excel report generation

---

## Project Structure

```
week7-sales-analysis/
│
├── sales_analyzer/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── reporter.py
│
├── data/
│   ├── raw/
│   │   └── sales_data.csv
│   ├── processed/
│   └── reports/
│
├── tests/
│   └── test_analyzer.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Features

### 🔹 Data Processing
- Load CSV/Excel sales datasets
- Validate required columns
- Remove duplicates
- Handle missing values
- Fix data types
- Remove invalid records

### 🔹 Business KPIs
- Total Sales
- Average Order Value (AOV)
- Total Orders
- Unique Customers
- Unique Products

### 🔹 Sales Analysis
- Category-wise revenue analysis
- Top-selling products
- Monthly sales trends
- Month-over-month growth calculation
- Moving average forecasting

### 🔹 Visualization
- Monthly sales trend line chart
- Category-wise bar chart
- Order value distribution histogram
- Saved as PNG files

### 🔹 Reporting
- Automated Excel report generation
- Executive summary text report
- Structured export of analysis results

### 🔹 Command-Line Interface (CLI)
Interactive menu for:
1. Basic Statistics
2. Category Analysis
3. Monthly Trends
4. Generate Visualizations
5. Generate Reports
6. Full Analysis Execution

---

## Sample Output

### Example KPI Output
```
📊 SALES SUMMARY
==============================
Total Sales: ₹8200.0
Average Order Value: ₹820.0
Total Orders: 10
Unique Customers: 5
Unique Products: 6
```

### Generated Reports
After running full analysis:

```
data/reports/
│
├── monthly_trend.png
├── category_sales.png
├── order_distribution.png
├── sales_report.xlsx
└── executive_summary.txt
```

---

## How to Run the Project

### 1️. Clone the Repository

```
git clone <your-repository-link>
cd week7-sales-analysis
```

### 2️. Install Dependencies

```
pip install -r requirements.txt
```

### 3️. Run the Application

```
python main.py
```

### 4. Choose Menu Option

Example:

```
Enter choice: 6
```

This will:
- Display KPIs
- Generate visualizations
- Export reports

---

## Running Tests

To run basic unit tests:

```
python -m pytest
```

---

## Business Use Case

This system simulates a real-world analytics workflow used by:

- Retail businesses
- E-commerce platforms
- Sales management teams
- Business intelligence departments

It transforms raw transactional data into actionable insights that help in:
- Identifying high-performing categories
- Tracking revenue growth
- Understanding customer distribution
- Supporting data-driven decision making

---

## Architecture Design

The project follows modular separation of concerns:

- `data_loader.py` → Data ingestion & validation  
- `data_cleaner.py` → Preprocessing pipeline  
- `analyzer.py` → KPI and trend computation  
- `visualizer.py` → Chart generation  
- `reporter.py` → Excel & text report export  
- `main.py` → CLI control layer  

This design improves:
- Maintainability
- Scalability
- Code readability
- Reusability

---

## Future Improvements

- Web-based dashboard using Streamlit
- Database integration (SQL)
- Interactive filtering
- Advanced forecasting models
- Deployment as a cloud service

---

## Author
Pranav Mali
Developed as part of internship project work to demonstrate practical data analytics and modular software design skills.
