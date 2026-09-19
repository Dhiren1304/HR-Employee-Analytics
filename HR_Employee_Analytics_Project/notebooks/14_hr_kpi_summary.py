
import pandas as pd
from pathlib import Path

# Find project folder automatically
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
DATA_FILE = BASE_DIR / "processed" / "hr_employee_cleaned.csv"
REPORTS_DIR = BASE_DIR / "reports"

# Create reports folder if needed
REPORTS_DIR.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_FILE)

# Basic KPI calculations
total_employees = len(df)

employees_left = (
    df["Attrition"] == "Yes"
).sum()

attrition_rate = (
    employees_left / total_employees * 100
)

retention_rate = 100 - attrition_rate

average_income = df["MonthlyIncome"].mean()
average_age = df["Age"].mean()
average_years_at_company = df["YearsAtCompany"].mean()

# Overtime attrition rate
overtime_total = df.groupby("OverTime").size()

overtime_left = (
    df[df["Attrition"] == "Yes"]
    .groupby("OverTime")
    .size()
)

overtime_attrition_rate = (
    overtime_left / overtime_total * 100
).fillna(0)

# Department attrition rate
department_total = df.groupby("Department").size()

department_left = (
    df[df["Attrition"] == "Yes"]
    .groupby("Department")
    .size()
)

department_attrition_rate = (
    department_left / department_total * 100
).fillna(0)

# Create KPI summary
kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Employees",
        "Employees Left",
        "Overall Attrition Rate (%)",
        "Retention Rate (%)",
        "Average Monthly Income",
        "Average Age",
        "Average Years at Company"
    ],
    "Value": [
        total_employees,
        employees_left,
        round(attrition_rate, 2),
        round(retention_rate, 2),
        round(average_income, 2),
        round(average_age, 2),
        round(average_years_at_company, 2)
    ]
})

# Display KPI summary
print("\nHR ANALYTICS KPI SUMMARY")
print("========================")
print(kpi_summary.to_string(index=False))

print("\nOVERTIME ATTRITION RATE (%)")
print("===========================")
print(overtime_attrition_rate.round(2))

print("\nDEPARTMENT ATTRITION RATE (%)")
print("=============================")
print(department_attrition_rate.round(2))

# Save KPI summary
kpi_file = REPORTS_DIR / "hr_kpi_summary.csv"
kpi_summary.to_csv(kpi_file, index=False)

# Save overtime analysis
overtime_file = REPORTS_DIR / "overtime_kpi_summary.csv"
overtime_attrition_rate.round(2).rename(
    "AttritionRate"
).to_csv(overtime_file)

# Save department analysis
department_file = REPORTS_DIR / "department_kpi_summary.csv"
department_attrition_rate.round(2).rename(
    "AttritionRate"
).to_csv(department_file)

print("\nFiles saved successfully:")
print(kpi_file)
print(overtime_file)
print(department_file)