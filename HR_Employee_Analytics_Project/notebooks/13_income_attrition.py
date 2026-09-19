
import pandas as pd
import matplotlib.pyplot as plt
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

# Create income groups
def create_income_group(income):
    if income < 3000:
        return "Below 3000"
    elif income <= 6000:
        return "3000-6000"
    elif income <= 10000:
        return "6001-10000"
    else:
        return "Above 10000"

df["IncomeGroup"] = df["MonthlyIncome"].apply(
    create_income_group
)

# Total employees in each income group
income_total = df.groupby("IncomeGroup").size()

# Employees who left in each income group
income_left = (
    df[df["Attrition"] == "Yes"]
    .groupby("IncomeGroup")
    .size()
)

# Calculate attrition rate
income_attrition_rate = (
    income_left / income_total * 100
).fillna(0)

# Arrange groups logically
group_order = [
    "Below 3000",
    "3000-6000",
    "6001-10000",
    "Above 10000"
]

income_attrition_rate = income_attrition_rate.reindex(
    group_order,
    fill_value=0
)

# Display results
print("\nIncome-wise Attrition Rate (%)")
print("--------------------------------")
print(income_attrition_rate.round(2))

# Create chart
ax = income_attrition_rate.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Monthly Income vs Employee Attrition")
plt.xlabel("Monthly Income Group")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)

# Add percentage labels
for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f%%",
        padding=3
    )

plt.tight_layout()

# Save chart
OUTPUT_FILE = REPORTS_DIR / "income_attrition_rate.png"
plt.savefig(OUTPUT_FILE, dpi=300)

print("\nChart saved successfully:")
print(OUTPUT_FILE)

plt.show()