import pandas as pd
import os

df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
print(df.head())
print(df.isnull().sum())

columns_to_drop = ["EmployeeCount", "Over18", "StandardHours"]
df = df.drop(columns=columns_to_drop)
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})
df["Gender"] = df["Gender"].astype("category")

print("\nData after cleaning")
print(df.head())
print("\nInformation about columns after cleaning:")
print(df.info())

# Ensure results directory exists
os.makedirs("../results", exist_ok=True)

categorical_cols = ["BusinessTravel", "Department", "JobRole", "MaritalStatus", "EducationField", "OverTime"]
for col in categorical_cols:
    df[col] = df[col].astype("category")

df["YearsAtCompanyRatio"] = df["YearsAtCompany"] / df["Age"]

print("Current working directory:", os.getcwd())  
df.to_csv("../data/HR_Attrition_Clean.csv", index=False)
print("File saved successfully in the current directory.")
