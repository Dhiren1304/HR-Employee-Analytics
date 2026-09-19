
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find the project folder automatically
BASE_DIR = Path(__file__).resolve().parent.parent

# Define file paths
DATA_FILE = BASE_DIR / "processed" / "hr_employee_cleaned.csv"
REPORTS_DIR = BASE_DIR / "reports"

# Create reports folder if it does not exist
REPORTS_DIR.mkdir(exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA_FILE)

# Calculate total employees by overtime status
overtime_total = df.groupby("OverTime").size()

# Calculate employees who left by overtime status
overtime_left = (
    df[df["Attrition"] == "Yes"]
    .groupby("OverTime")
    .size()
)

# Calculate attrition rate
overtime_attrition_rate = (
    overtime_left / overtime_total * 100
).fillna(0)

# Display results
print("\nOvertime-wise Attrition Rate (%)")
print("---------------------------------")
print(overtime_attrition_rate.round(2))

# Create chart
ax = overtime_attrition_rate.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Overtime-wise Employee Attrition Rate")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)

# Add percentage labels
for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%")

plt.tight_layout()

# Save chart
OUTPUT_FILE = REPORTS_DIR / "overtime_attrition_rate.png"
plt.savefig(OUTPUT_FILE, dpi=300)

print("\nChart saved successfully:")
print(OUTPUT_FILE)

plt.show()