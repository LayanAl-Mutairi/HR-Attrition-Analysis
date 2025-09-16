import streamlit as st
from PIL import Image
import os

# Page config 
st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")

st.title("📊 HR Attrition Interactive Dashboard")
st.markdown("Explore HR attrition insights interactively.")

# Directories 
plots_dir = "results"

# Define plots and categories 
plots = {
    "Attrition Overview": [
        ("overall_resignation_rate.png", "Overall Resignation Rate")
    ],
    "Salary Analysis": [
        ("avg_salary_by_department.png", "Average Salary by Department"),
        ("top5_job_roles_resignations.png", "Top 5 Job Roles with Resignations")
    ],
    "Demographics & Attrition": [
        ("attrition_gender_agegroup.png", "Attrition by Gender & Age Group"),
        ("high_risk_employees.png", "High-Risk Employees"),
        ("attrition_education_field.png", "Attrition by Education Field")
    ],
    "Work & Performance": [
        ("attrition_overtime.png", "Attrition by OverTime"),
        ("attrition_worklifebalance.png", "Attrition by Work-Life Balance"),
        ("attrition_years_company.png", "Attrition vs Years at Company"),
        ("attrition_last_promotion.png", "Attrition vs Years Since Last Promotion")
    ]
}

# Sidebar navigation 
category = st.sidebar.selectbox("Select Category", list(plots.keys()))
st.sidebar.markdown("---")
st.sidebar.markdown("Select a plot below:")

plot_names = [title for _, title in plots[category]]
selected_plot = st.sidebar.radio("", plot_names)

# Display plots in grid 
cols = st.columns(3)
i = 0
for file_name, title in plots[category]:
    col = cols[i % 3]
    img_path = os.path.join(plots_dir, file_name)
    col.image(Image.open(img_path), caption=title, use_column_width=True)
    i += 1

# Display selected plot enlarged  
st.markdown("---")
st.subheader(f"📌 {selected_plot}")
# Find corresponding file
for file_name, title in plots[category]:
    if title == selected_plot:
        img_path = os.path.join(plots_dir, file_name)
        st.image(Image.open(img_path), use_column_width=True)
        break
