# 📊 HR Attrition Analysis

 This project is for educational purposes only, to showcase skills in data cleaning, ETL, SQL analysis, and data visualization.
## 📂 Dataset
The dataset used in this project is the IBM HR Analytics Employee Attrition & Performance dataset from Kaggle. 
It contains information about employees, such as demographics, job roles, department, salary, work experience, performance, and attrition status. 

- Source: [Kaggle Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Number of records: 1470 employees
- Key features: Age, Gender, Department, JobRole, MonthlyIncome, YearsAtCompany, Attrition, WorkLifeBalance, OverTime, EducationField

## 🚀 Features / Project Highlights
This project provides the following analyses and insights based on the HR Attrition dataset:

1. 📈 **Overall Attrition Rate (%)** – Calculated using SQL query on the entire EmployeeData table.
2. 💰 **Average Salary per Department** – Shows which departments have higher/lower average income.
3. 🚪 **Top 5 Job Roles with Most Resignations** – Identifies roles contributing most to attrition.
4. 👥 **Attrition Rate by Gender & Age Group** – Insights into demographics with higher attrition.
5. ⚠️ **High-Risk Employees** – Identifies young employees with low salary and short tenure.
6. ⏳ **Attrition vs. Years at Company** – How employee tenure relates to attrition likelihood.
7. 🎓 **Attrition by Education Field** – Determines if education background impacts attrition.
8. 🕒 **Attrition by Overtime (Yes/No)** – Examines correlation between overtime work and resignations.
9. ⚖️ **Attrition Rate by Work-Life Balance** – Shows how work-life balance levels impact employee attrition.
10.🏆 **Attrition vs. Years Since Last Promotion** – Examines if promotion frequency affects attrition.
## 📁 Project Structure

IBM-HR-Attrition-Analysis/
├── data/
│   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   └── HR_Attrition_Clean.csv
├── scripts/
│   ├── 01_data_cleaning_and_eda.py
│   ├── 02_etl_to_sql.py
│   └── 03_analysis_visual.py
├── results/
│      ├── overall_resignation_rate.png
│      ├── avg_salary_by_department.png
│      ├── top5_job_roles_resignations.png
│      ├── attrition_gender_agegroup.png
│      ├── high_risk_employees.png
│      ├── attrition_overtime.png
│      ├── attrition_worklifebalance.png
│      ├── attrition_years_company.png
│      ├── attrition_last_promotion.png
│      └── attrition_education_field.png
├── HR_Attrition.db
├── dashboard.py          
├── requirements.txt
└── README.md

## 🛠️ How to Run

1. Clone this repository.
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run scripts in order:
```bash
python scripts/01_data_cleaning_and_eda.py
python scripts/02_etl_to_sql.py
python scripts/03_analysis_visual.py
```
## 📊 Results
All visualizations are saved in the `results/` folder.  
- Charts and plots (PNG) include overall attrition rate, average salary by department, top job roles with resignations, attrition by gender, age group, overtime, work-life balance, years at company, last promotion, and education field.


## 🖥️ Interactive Dashboard
Explore HR Attrition insights interactively with a Streamlit Dashboard.
Grid view: See all charts together for easy comparison.
Enlarge charts: Select any chart to view in full size.
Fully interactive: Scroll, zoom, and explore insights without coding.
```bash
pip install streamlit
streamlit run dashboard.py
```

## ✍️ Author 
Name : Layan AlMutairi 
Email : layanal-mutairi@outlook.sa