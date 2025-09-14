import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")
st.title("📊 HR Attrition Interactive Dashboard")

# Directory with saved plots
plots_dir = "results"

# List of plot files and titles
plot_files = [
    "overall_resignation_rate.png",
    "avg_salary_by_department.png",
    "top5_job_roles_resignations.png",
    "attrition_gender_agegroup.png",
    "high_risk_employees.png",
    "attrition_overtime.png",
    "attrition_worklifebalance.png",
    "attrition_years_company.png",
    "attrition_last_promotion.png",
    "attrition_education_field.png"
]

plot_titles = [
    "Overall Resignation Rate",
    "Average Salary by Department",
    "Top 5 Job Roles with Resignations",
    "Attrition by Gender & Age Group",
    "High-Risk Employees",
    "Attrition by OverTime",
    "Attrition by Work-Life Balance",
    "Attrition vs Years at Company",
    "Attrition vs Years Since Last Promotion",
    "Attrition by Education Field"
]

# Dropdown to enlarge a selected chart
selected_plot = st.selectbox("Select a chart to enlarge:", plot_titles)

# Display thumbnails in grid (3 per row)
cols = st.columns(3)
for i, plot_file in enumerate(plot_files):
    col = cols[i % 3]
    image_path = os.path.join(plots_dir, plot_file)
    col.image(Image.open(image_path), caption=plot_titles[i], use_column_width=True)

# Display the selected chart in large view
st.markdown("---")
st.subheader(f"📌 {selected_plot}")
index = plot_titles.index(selected_plot)
image_path = os.path.join(plots_dir, plot_files[index])
st.image(Image.open(image_path), use_column_width=True)
