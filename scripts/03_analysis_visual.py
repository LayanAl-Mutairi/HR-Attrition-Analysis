import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid", font_scale=1.1)
plt.rcParams["figure.figsize"] = (10,6)

# Ensure results directories exist
os.makedirs("../results", exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("../HR_Attrition.db")

#  Overall Attrition Rate (Donut Chart)
df1 = pd.read_sql("SELECT ROUND(AVG(Attrition)*100, 2) as AttritionRate FROM EmployeeData;", conn)
print("📊 Overall Resignation Rate (%):\n", df1)

plt.figure(figsize=(6,6))
sizes = [df1['AttritionRate'][0], 100 - df1['AttritionRate'][0]]
labels = ['Resigned', 'Stayed']
colors = ['#ff9999', '#66b3ff']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'fontsize':12})
centre_circle = plt.Circle((0,0),0.50,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("📊 Overall Resignation Rate (%)", fontsize=16)
plt.tight_layout()
plt.savefig("../results/overall_resignation_rate.png")
plt.close()

#  Avg Salary per Department (Vertical Bar)
df2 = pd.read_sql("""
SELECT Department, ROUND(AVG(MonthlyIncome), 2) as AvgIncome
FROM EmployeeData
GROUP BY Department
ORDER BY AvgIncome DESC;
""", conn)
print("\n💰 Average Salaries by Department:\n", df2)

plt.figure(figsize=(12,6))
ax = sns.barplot(x='Department', y='AvgIncome', data=df2, palette="viridis")
plt.title("Average Salary by Department", fontsize=14)
plt.ylabel("Average Salary")
plt.xlabel("Department")
plt.xticks(rotation=45, ha='right')
for p in ax.patches:
    ax.annotate(f"{p.get_height():,.0f}", (p.get_x()+p.get_width()/2., p.get_height()),
                ha='center', va='bottom', fontsize=10, color='black')
plt.tight_layout()
plt.savefig("../results/avg_salary_by_department.png")
plt.close()

#  Top 5 Job Roles with most resignations (Horizontal Bar)
df3 = pd.read_sql("""
SELECT JobRole, SUM(Attrition) as NumAttrition
FROM EmployeeData
GROUP BY JobRole
ORDER BY NumAttrition DESC
LIMIT 5;
""", conn)
print("\n🚪 Top 5 Job Roles with Resignations:\n", df3)

plt.figure(figsize=(10,6))
ax = sns.barplot(x='NumAttrition', y='JobRole', data=df3, palette="rocket")
plt.title("Top 5 Job Roles with Resignations", fontsize=14)
plt.xlabel("Number of Resignations")
plt.ylabel("Job Role")
for i, v in enumerate(df3['NumAttrition']):
    ax.text(v + 0.1, i, str(v), color='black', va='center', fontsize=11)
plt.tight_layout()
plt.savefig("../results/top5_job_roles_resignations.png")
plt.close()

#  Attrition Rate by Gender & Age Group (Grouped Barplot)
df4 = pd.read_sql("""
SELECT Gender,
       CASE 
         WHEN Age < 30 THEN 'Under 30'
         WHEN Age BETWEEN 30 AND 40 THEN '30-40'
         WHEN Age BETWEEN 41 AND 50 THEN '41-50'
         ELSE '50+' 
       END as AgeGroup,
       ROUND(AVG(Attrition)*100,2) as AttritionRate
FROM EmployeeData
GROUP BY Gender, AgeGroup
ORDER BY AgeGroup;
""", conn)
print("\n📊 Attrition Rate by Gender & Age Group:\n", df4)

plt.figure(figsize=(10,6))
sns.barplot(x='AgeGroup', y='AttritionRate', hue='Gender', data=df4, palette="pastel")
plt.title("Attrition Rate by Gender & Age Group", fontsize=14)
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Age Group")
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig("../results/attrition_gender_agegroup.png")
plt.close()

#  High Risk Employees (Countplot Horizontal)
df5 = pd.read_sql("""
SELECT EmployeeNumber, JobRole, Age, MonthlyIncome, YearsAtCompany, Attrition
FROM EmployeeData
WHERE Age < 30 AND MonthlyIncome < 5000 AND YearsAtCompany < 3;
""", conn)
print("\n⚠️ High Risk Employees:\n", df5.head(10))

plt.figure(figsize=(10,6))
ax = sns.countplot(y='JobRole', data=df5, palette="magma", order=df5['JobRole'].value_counts().index)
plt.title("High Risk Employees by Job Role (Top 10)", fontsize=14)
plt.xlabel("Count")
plt.ylabel("Job Role")
for i, v in enumerate(df5['JobRole'].value_counts()):
    ax.text(v + 0.1, i, str(v), color='black', va='center', fontsize=11)
plt.tight_layout()
plt.savefig("../results/high_risk_employees.png")
plt.close()

#  Attrition Rate by OverTime (Barplot)
df6 = pd.read_sql("""
SELECT OverTime,
       ROUND(AVG(Attrition)*100,2) as AttritionRate
FROM EmployeeData
GROUP BY OverTime;
""", conn)
print("\n🕒 Attrition Rate by OverTime:\n", df6)

plt.figure(figsize=(6,6))
sns.barplot(x='OverTime', y='AttritionRate', data=df6, palette="coolwarm")
plt.title("Attrition Rate by OverTime", fontsize=14)
plt.ylabel("Attrition Rate (%)")
plt.xlabel("OverTime")
for i, v in enumerate(df6['AttritionRate']):
    plt.text(i, v + 0.5, f"{v}%", ha='center', fontsize=11)
plt.tight_layout()
plt.savefig("../results/attrition_overtime.png")
plt.close()

#  Attrition Rate by WorkLifeBalance (Barplot)
df7 = pd.read_sql("""
SELECT WorkLifeBalance,
       ROUND(AVG(Attrition)*100,2) as AttritionRate
FROM EmployeeData
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;
""", conn)
print("\n⚖️ Attrition Rate by WorkLifeBalance:\n", df7)

plt.figure(figsize=(7,6))
sns.barplot(x='WorkLifeBalance', y='AttritionRate', data=df7, palette="Set2")
plt.title("Attrition Rate by Work-Life Balance", fontsize=14)
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Work-Life Balance (1=Bad, 4=Excellent)")
for i, v in enumerate(df7['AttritionRate']):
    plt.text(i, v + 0.5, f"{v}%", ha='center', fontsize=11)
plt.tight_layout()
plt.savefig("../results/attrition_worklifebalance.png")
plt.close()

#  Attrition vs YearsSinceLastPromotion (Lineplot)
df8 = pd.read_sql("""
SELECT YearsSinceLastPromotion,
       ROUND(AVG(Attrition)*100,2) as AttritionRate
FROM EmployeeData
GROUP BY YearsSinceLastPromotion
ORDER BY YearsSinceLastPromotion;
""", conn)
print("\n📈 Attrition Rate by Years Since Last Promotion:\n", df8)

plt.figure(figsize=(10,6))
sns.lineplot(x='YearsSinceLastPromotion', y='AttritionRate', data=df8, marker='o', color='purple')
plt.title("Attrition Rate by Years Since Last Promotion", fontsize=14)
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Years Since Last Promotion")
for x, y in zip(df8['YearsSinceLastPromotion'], df8['AttritionRate']):
    plt.text(x, y+0.5, f"{y}%", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig("../results/attrition_last_promotion.png")
plt.close()

#  Attrition vs Years at Company (Lineplot)
df9 = pd.read_sql("""
SELECT YearsAtCompany,
       ROUND(AVG(Attrition)*100,2) as AttritionRate
FROM EmployeeData
GROUP BY YearsAtCompany
ORDER BY YearsAtCompany;
""", conn)
print("\n📅 Attrition Rate by Years at Company:\n", df9)

plt.figure(figsize=(10,6))
sns.lineplot(x='YearsAtCompany', y='AttritionRate', data=df9, marker='o', color='green')
plt.title("Attrition Rate by Years at Company", fontsize=14)
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Years at Company")
for x, y in zip(df9['YearsAtCompany'], df9['AttritionRate']):
    plt.text(x, y+0.5, f"{y}%", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig("../results/attrition_years_company.png")
plt.close()

#  Attrition by Education Field (Barplot)
df10 = pd.read_sql("""
SELECT EducationField,
       ROUND(AVG(Attrition)*100,2) as AttritionRate
FROM EmployeeData
GROUP BY EducationField
ORDER BY AttritionRate DESC;
""", conn)
print("\n🎓 Attrition Rate by Education Field:\n", df10)

plt.figure(figsize=(10,6))
ax = sns.barplot(x='EducationField', y='AttritionRate', data=df10, palette="Spectral")
plt.title("Attrition Rate by Education Field", fontsize=14)
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Education Field")
for p in ax.patches:
    ax.annotate(f"{p.get_height():.1f}%", (p.get_x()+p.get_width()/2., p.get_height()),
                ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../results/attrition_education_field.png")
plt.close()

# Close the database connection
conn.close()
