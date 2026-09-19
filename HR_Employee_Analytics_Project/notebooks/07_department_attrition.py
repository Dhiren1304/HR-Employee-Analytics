
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(
    "../processed/hr_employee_cleaned.csv"
)

# Create department-wise attrition table
department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

print("Department-wise Attrition:")
print(department_attrition)

# Create chart
department_attrition.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Department-wise Employee Attrition")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)
plt.legend(title="Attrition")

plt.tight_layout()

# Save chart
plt.savefig(
    "../reports/department_attrition.png",
    dpi=300
)

plt.show()