# 🧠 Automated Report Generator

The **Automated Report Generator** is a Streamlit-based Python application that automates the process of **data analysis**, **visualization**, and **report generation** in PDF format.

It supports **Sales**, **HR**, and **Finance** datasets and can automatically generate KPIs, insights, and visual reports with just a few clicks.

---

## 🚀 Features

✅ **Upload any dataset (Sales, HR, or Finance)**
✅ **Automatic preprocessing and data cleaning**
✅ **Dynamic column mapping support**
✅ **KPI calculation for each dataset type**
✅ **Data visualizations using Matplotlib & Plotly**
✅ **PDF report generation using ReportLab**
✅ **Streamlit interface for user interaction**


---

## 🧩 Tech Stack

* **Python 3.12+**
* **Streamlit** – Interactive UI
* **Pandas & NumPy** – Data manipulation
* **Matplotlib, Seaborn & Plotly** – Data visualization
* **ReportLab** – PDF report generation
* **python-dotenv** – Environment variable management

---

## 🗂️ Project Structure

```

├── src/
│   ├── data/                        # Uploaded input datasets
│   ├── temp/                        # Temporary uploaded files               
│   │
│   ├── analysis.py                  # KPIs & visualizations
│   ├── app.py                       # Data loading, preprocessing, KPI logic
│   ├── report_generator.py          # PDF creation logic
│   ├── streamlit_app.py             # Streamlit UI
│   ├── utils.py                     # Helper functions
│   │
│   ├── requirements.txt             # Dependencies
|── .gitignore                       # Ignore unnecessary files
└── .venv/                           # Virtual environment

```




## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/Automated_Report_Generator.git
cd Automated_Report_Generator
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

* On Windows:

  ```bash
  .venv\Scripts\activate
  ```
* On macOS/Linux:

  ```bash
  source .venv/bin/activate
  ```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 How to Run

### ▶️ Run Streamlit App

```bash
streamlit run streamlit_app.py
```

Upload your dataset via the Streamlit UI and select the **data type** (Sales / HR / Finance) from the dropdown.
The app will automatically:

* Preprocess and clean your dataset
* Calculate KPIs
* Generate visualizations
* Export a professional PDF report

You can download the report directly from the app.
---

## 📊 Supported Datasets & Columns

| Data Type | Required Columns                                     |
| --------- | ---------------------------------------------------- |
| Sales     | Date, Product, Region, Sales, Profit                 |
| HR        | Employee_ID, Salary, Department, Attrition, Location |
| Finance   | Account, Expense, Revenue, Month, Region             |

---

## 🧠 Future Enhancements

* Add database connectivity (MySQL / PostgreSQL)
* Integrate email templates for rich reports
* Add more dataset categories (e.g., Marketing, Logistics)
* Add dashboard export feature

---

## 🤝 Contributing

Pull requests are welcome!
If you’d like to add features or fix issues:

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

---

## 🧑‍💻 Author

**Abhinav Bisht**
📧 abhinavworking11@gmail.com
💼 [GitHub Profile](https://github.com/<your-username>)

---

## 🪪 License

This project is licensed under the MIT License — feel free to use and modify it.

---

✨ **“Automate insights, save time, and generate reports in seconds.”**
