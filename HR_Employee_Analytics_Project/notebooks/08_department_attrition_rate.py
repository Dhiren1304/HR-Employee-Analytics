
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(
    "../processed/hr_employee_cleaned.csv"
)

# Calculate total employees per department
department_total = df.groupby(
    "Department"
).size()

# Calculate employees who left per department
department_left = df[
    df["Attrition"] == "Yes"
].groupby(
    "Department"
).size()

# Calculate attrition rate
department_attrition_rate = (
    department_left / department_total * 100
).fillna(0).sort_values(ascending=False)

print("Department-wise Attrition Rate (%):")
print(department_attrition_rate.round(2))

# Create chart
plt.figure(figsize=(10, 6))

department_attrition_rate.plot(
    kind="bar"
)

plt.title("Department-wise Attrition Rate")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig(
    "../reports/department_attrition_rate.png",
    dpi=300
)

plt.show()