import sqlite3
import pandas as pd
import os
df = pd.read_csv("../data/HR_Attrition_Clean.csv")
conn = sqlite3.connect("../HR_Attrition.db")
df.to_sql("EmployeeData", conn, if_exists="replace", index=False)
conn.close()
print("✅ Data uploaded to SQLite database successfully.")
