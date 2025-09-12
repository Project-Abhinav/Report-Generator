# utils.py

from datetime import datetime

def create_summary(kpis, file_type):
    if file_type == "Sales":
        return f"This week, total sales reached {kpis.get('Total Sales', 'N/A')} with {kpis.get('Best Product', 'N/A')} being the top-selling product."
    elif file_type == "HR":
        return f"Current headcount is {kpis.get('Headcount', 'N/A')} with an average salary of {kpis.get('Average Salary', 'N/A')}."
    elif file_type == "Finance":
        return f"This month, total revenue is {kpis.get('Total Revenue', 'N/A')} against expenses of {kpis.get('Total Expense', 'N/A')}."
    else:
        return "Report Summary"

def get_chart_paths(file_type):
    base_path = "chart/"
    if file_type == "Sales":
        return [base_path + "sales_trend.png", base_path + "top_products.png", base_path + "region_sales.png"]
    elif file_type == "HR":
        return [base_path + "hr_salary_dist.png", base_path + "hr_attrition.png", base_path + "hr_department.png"]
    elif file_type == "Finance":
        return [base_path + "finance_trend.png", base_path + "finance_pie.png", base_path + "finance_expense.png"]
    else:
        return []
