import pandas as pd
from analysis import Calculate_Sales_kpi,print_Sales_kpis,Calculate_HR_kpis,calculate_finance_kpis,print_finance_kpis,print_hr_kpis,visualize_sales,visualize_hr,visualize_finance
from utils import create_summary, get_chart_paths
from report_generator import generate_pdf



file_type = "Sales"

if file_type == "Sales":
    required_columns = ['Date','Product','Region','Sales','Profit']

elif file_type == "HR":
    required_columns = ['Employes_ID','Salary','Department','Attrition','Location']

elif file_type == "Finance":
    required_columns = ['Account','Expense','Revenue','Month','Region']

else :
    print("Please upload a file that have data related to Sales, HR, Finance.We currently support only thse 3 data.")   

def load_file(file_path):

    try :

        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)

        elif file_path.endswith(('.xlx','.xlsx')):
            df = pd.read_excel(file_path)
        
        else :
            raise ValueError("Unsupported file format. Please upload CSV or Excel files.")
        
        print("File loaded successfully!")
        return df
    
    except Exception as e :
        print(f"Error loading file: {e}")
        return None

def apply_mapping(df,mapping):
    df = df.rename(columns = {v:k for k,v in mapping.items()})
    return df

def validate_columns(df,required_columns):
    missing_cols = [col for col in required_columns if col not in df.columns]

    if missing_cols:
        print(f"Missing columns after mappings:{missing_cols}")
        return False
    
    else:
        print("All required columns are present after mapping!")
        return True
    
def preprocess_data(df) :

    df = df.fillna(0)
    df = df.dropna(how="all")
    df = df.drop_duplicates()

    if file_type == "Sales":

        if "Date" in df.columns:
            df['Date'] = pd.to_datetime(df['Date'],errors='coerce')

        for col in ['Sales','Profit']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col],errors='coerce').fillna(0)

    elif file_type == "HR":
        if 'Salary' in df.columns:
            df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce').fillna(0)

    elif file_type == 'Finance':
        if 'Month' in df.columns:
            df['Month'] = pd.to_datetime(df['Month'], errors='coerce')

        if 'Expense' in df.columns:
            df['Expense'] = pd.to_numeric(df['Expense'], errors='coerce').fillna(0)
        if 'Revenue' in df.columns:
            df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce').fillna(0)

    
    print("File is now ready to use ")
    return df


def main(file_path):
    
    df = load_file(file_path)
    if df is None:
        return
    
    mapping = {
    'Date': 'Order_Date',
    'Product': 'Product_Category',
    'Region': 'City',
    'Sales': 'Sales_Amount',
    'Profit': 'Profit'
}
    
    print("\nApplying column mapping...")
    df = apply_mapping(df, mapping)

    if not validate_columns(df, required_columns):
        print("Please ensure the columns are mapped correctly and try again.")
        print(f"\n Please Ensure that your Data must have Columns that can Relate to these Columns: {[x for x in required_columns]} ")
        return

    df = preprocess_data(df)

    print("✅ Data preprocessing completed!")
    print("\nPreview of cleaned data:")
    print(df.head())

    if file_type == "Sales":
    
        kpis = Calculate_Sales_kpi(df)
        print_Sales_kpis(kpis)
        visualize_sales(df)


    elif file_type == "HR":
        kpis = Calculate_HR_kpis(df)
        print_hr_kpis(kpis)
        visualize_hr(df)

    else : 
        kpis = calculate_finance_kpis(df)
        print_finance_kpis(kpis)
        visualize_finance(df)

    summary_text = create_summary(kpis, file_type)
    chart_paths = get_chart_paths(file_type)
    output_file = output_file = "output/weekly_report.pdf"

    generate_pdf(kpis, summary_text, chart_paths, output_file)

if __name__ == "__main__":
    
    file_path = "data/Snitch_Fashion_Sales_Uncleaned.csv"
    main(file_path)