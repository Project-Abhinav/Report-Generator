import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


def visualize_sales(df):
    print("\n📊 Generating Sales Visualizations...")

    if "Date" in df.columns and "Sales" in df.columns:

        plt.figure(figsize=(10,5))
        sales_df = df.groupby("Date")["Sales"].sum().reset_index()
        sns.lineplot(data=sales_df,x="Date",y="Sales")
        plt.title('Sales Trend Over Time')
        plt.xticks(rotation = 45)
        plt.tight_layout()
        plt.savefig("chart/sales_trend.png")
        plt.close()

    if 'Product' in df.columns and 'Sales' in df.columns:
        plt.figure(figsize=(10, 5))
        top_products_df = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
        sns.barplot(x=top_products_df.index, y=top_products_df.values)
        plt.title('Top 5 Products by Sales')
        plt.tight_layout()
        plt.savefig('chart/top_products.png')
        plt.close()

    if 'Region' in df.columns and 'Sales' in df.columns:
        plt.figure(figsize=(10,8))
        top_Region_df = df.groupby("Region")["Sales"].sum()
        top_Region_df = top_Region_df.sample(frac=1)
        plt.pie(top_Region_df.values,labels=top_Region_df.index,autopct="%1.1f%%", startangle = 90,labeldistance=1.1, pctdistance=0.85)
        plt.title("Sales Contribution by Region")
        plt.tight_layout()
        plt.savefig("chart/region_sales.png")
        plt.close()

    print("✅  visualizations Completed!")

def visualize_hr(df):

        print("\n📊 Generating HR Visualizations...")

        # Bar chart - Employees by Department
        if 'Department' in df.columns:
            plt.figure(figsize=(10, 5))
            df_dept = df['Department'].value_counts()
            sns.barplot(x=df_dept.index, y=df_dept.values)
            plt.title('Employees by Department')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('chart/hr_department.png')
            plt.close()

        # Pie chart - Attrition rate
        if 'Attrition' in df.columns:
            plt.figure(figsize=(10, 8))
            df_attrition = df['Attrition'].value_counts()
            plt.pie(df_attrition, labels=df_attrition.index, autopct='%1.1f%%', startangle=90,labeldistance=1.1, pctdistance=0.85)
            plt.title('Attrition Rate')
            plt.tight_layout()
            plt.savefig('chart/hr_attrition.png')
            plt.close()

        # Histogram - Salary distribution
        if 'Salary' in df.columns:
            plt.figure(figsize=(10, 5))
            sns.histplot(df['Salary'], bins=20, kde=True)
            plt.title('Salary Distribution')
            plt.tight_layout()
            plt.savefig('chart/hr_salary_dist.png')
            plt.close()

        print("✅  visualizations Completed!")

def visualize_finance(df):

        print("\n📊 Generating Finance Visualizations...")

        # Line chart - Revenue and Expense over time
        if 'Month' in df.columns and ('Revenue' in df.columns or 'Expense' in df.columns):
            plt.figure(figsize=(10, 5))
            df_grouped = df.groupby('Month')[['Revenue', 'Expense']].sum().reset_index()
            sns.lineplot(data=df_grouped, x='Month', y='Revenue', label='Revenue')
            sns.lineplot(data=df_grouped, x='Month', y='Expense', label='Expense')
            plt.title('Monthly Revenue vs Expense')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('chart/finance_trend.png')
            plt.close()

        # Bar chart - Top 5 expense accounts
        if 'Account' in df.columns and 'Expense' in df.columns:
            plt.figure(figsize=(10, 5))
            df_acc = df.groupby('Account')['Expense'].sum().sort_values(ascending=False).head(5)
            sns.barplot(x=df_acc.index, y=df_acc.values)
            plt.title('Top 5 Expense Categories')
            plt.tight_layout()
            plt.savefig('chart/finance_expense.png')
            plt.close()

        # Pie chart - Revenue vs Expense
        if 'Revenue' in df.columns and 'Expense' in df.columns:
            plt.figure(figsize=(10, 8))
            total_revenue = df['Revenue'].sum()
            total_expense = df['Expense'].sum()
            plt.pie([total_revenue, total_expense], labels=['Revenue', 'Expense'], autopct='%1.1f%%', startangle=90,labeldistance=1.1, pctdistance=0.85)
            plt.title('Revenue vs Expense')
            plt.tight_layout()
            plt.savefig('chart/finance_pie.png')
            plt.close()

        print("✅  visualizations Completed!")