
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(
    "../processed/hr_employee_cleaned.csv"
)

# Count attrition categories
attrition_counts = df["Attrition"].value_counts()

# Create bar chart
plt.figure(figsize=(8, 5))

attrition_counts.plot(kind="bar")

plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig(
    "../reports/attrition_distribution.png",
    dpi=300
)

# Display chart
plt.show()