
import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../processed/hr_employee_cleaned.csv"
)

print("========== DATASET OVERVIEW ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# 1. Count employees by attrition
print("\n========== ATTRITION COUNTS ==========")

attrition_counts = df["Attrition"].value_counts()

print(attrition_counts)


# 2. Calculate attrition rate
print("\n========== ATTRITION RATE ==========")

total_employees = len(df)

employees_left = (df["Attrition"] == "Yes").sum()

attrition_rate = (
    employees_left / total_employees
) * 100

print("Total Employees:", total_employees)
print("Employees Who Left:", employees_left)
print("Attrition Rate:", round(attrition_rate, 2), "%")


# 3. Calculate retention rate
print("\n========== RETENTION RATE ==========")

retention_rate = 100 - attrition_rate

print("Retention Rate:", round(retention_rate, 2), "%")

