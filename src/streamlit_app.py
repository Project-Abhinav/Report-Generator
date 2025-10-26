import streamlit as st
import pandas as pd
import os
from app import main, get_required_columns

st.set_page_config(page_title="Automated Report Generator", layout="wide")

st.title("📊 Automated Report Generator")

uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xls", "xlsx"])
file_type = st.selectbox("Select the dataset type", ["Sales", "HR", "Finance"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")
        st.dataframe(df.head())

        required_columns = get_required_columns(file_type)
        mapping = {}

        st.subheader("Column Mapping")
        st.write("Map the required columns to your dataset columns.")

        for col in required_columns:
            mapping[col] = st.selectbox(f"Map '{col}' to:", options=df.columns, index=0)

        if st.button("Generate Report"):
            # Save the uploaded file temporarily
            os.makedirs("temp", exist_ok=True)
            temp_file = f"temp/{uploaded_file.name}"
            with open(temp_file, "wb") as f:
                f.write(uploaded_file.getbuffer())

            output_file = main(temp_file, file_type, mapping)

            if output_file:
                with open(output_file, "rb") as f:
                    st.download_button(
                        label="📥 Download Report",
                        data=f,
                        file_name=os.path.basename(output_file),
                        mime="application/pdf"
                    )
                st.success("Report generated successfully!")
            else:
                st.error("Report generation failed. Please check your mappings and input file.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
