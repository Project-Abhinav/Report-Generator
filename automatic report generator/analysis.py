import pandas as pd
import matplotlib.pyplot as plt

def Calculate_Sales_kpi(df):

    kpis = {}

    kpis['Total Sales'] = df['Sales'].sum()

    # Best region by total sales

    region_sales = df.groupby('Region')['Sales'].sum()
    kpis['Best Region'] = region_sales.idxmax()

    #Best product by total sales

    best_product = df.groupby('Product')['Sales'].sum()
    kpis['Best Product'] = best_product.idxmax()

    kpis['Total Profit'] = df['Profit'].sum()

    return kpis

def print_Sales_kpis(kpis):
  
    
    print("\n📊 Key Performance Indicators (KPIs):")
    print(f"✔ Total Sales    : ₹{kpis['Total Sales']}")
    print(f"✔ Best Region    : {kpis['Best Region']}")
    print(f"✔ Best Product   : {kpis['Best Product']}")
    print(f"✔ Total Profit   : ₹{kpis['Total Profit']}")

def Calculate_HR_kpis(df):
    kpis = {}
    kpis['Total Employees'] = df['Employee_ID'].nunique()
    kpis['Average Salary'] = df['Salary'].mean()

    if 'Attrition' in df.columns:
        kpis['Attrition Rate (%)'] = (df['Attrition'].sum() / len(df)) * 100
    else:
        kpis['Attrition Rate (%)'] = 0

    return kpis

def print_hr_kpis(kpis):
    print("\n📊 HR KPIs:")
    print(f"✔ Total Employees   : {kpis['Total Employees']}")
    print(f"✔ Average Salary    : ₹{kpis['Average Salary']:.2f}")
    print(f"✔ Attrition Rate   : {kpis['Attrition Rate (%)']:.2f}%")

def calculate_finance_kpis(df):
    kpis = {}
    if 'Revenue' in df.columns:
        kpis['Total Revenue'] = df['Revenue'].sum()
    else:
        kpis['Total Revenue'] = 0

    if 'Expense' in df.columns:
        kpis['Total Expense'] = df['Expense'].sum()
    else:
        kpis['Total Expense'] = 0

    kpis['Net Profit'] = kpis['Total Revenue'] - kpis['Total Expense']

    if 'Expense' in df.columns and not df['Expense'].isnull().all():
        highest_expense = df.groupby('Account')['Expense'].sum().idxmax()
        kpis['Highest Expense Category'] = highest_expense
    else:
        kpis['Highest Expense Category'] = "N/A"

    return kpis

def print_finance_kpis(kpis):
    print("\n📊 Finance KPIs:")
    print(f"✔ Total Revenue          : ₹{kpis['Total Revenue']:.2f}")
    print(f"✔ Total Expense          : ₹{kpis['Total Expense']:.2f}")
    print(f"✔ Net Profit             : ₹{kpis['Net Profit']:.2f}")
    print(f"✔ Highest Expense Category : {kpis['Highest Expense Category']}")


