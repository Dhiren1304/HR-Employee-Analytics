
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

# Create tenure groups
def create_tenure_group(years):
    if years <= 2:
        return "0-2 Years"
    elif years <= 5:
        return "3-5 Years"
    elif years <= 10:
        return "6-10 Years"
    else:
        return "11+ Years"

df["TenureGroup"] = df["YearsAtCompany"].apply(
    create_tenure_group
)

# Calculate total employees in each group
tenure_total = df.groupby(
    "TenureGroup"
).size()

# Calculate employees who left
tenure_left = (
    df[df["Attrition"] == "Yes"]
    .groupby("TenureGroup")
    .size()
)

# Calculate attrition rate
tenure_attrition_rate = (
    tenure_left / tenure_total * 100
).fillna(0)

# Arrange groups in logical order
group_order = [
    "0-2 Years",
    "3-5 Years",
    "6-10 Years",
    "11+ Years"
]

tenure_attrition_rate = tenure_attrition_rate.reindex(
    group_order
)

# Display results
print("\nTenure-wise Attrition Rate (%)")
print("--------------------------------")
print(tenure_attrition_rate.round(2))

# Create chart
ax = tenure_attrition_rate.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Years at Company vs Employee Attrition")
plt.xlabel("Tenure Group")
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
OUTPUT_FILE = REPORTS_DIR / "tenure_attrition_rate.png"
plt.savefig(OUTPUT_FILE, dpi=300)

print("\nChart saved successfully:")
print(OUTPUT_FILE)

plt.show()