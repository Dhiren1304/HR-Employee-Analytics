
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

# Total employees in each job role
jobrole_total = df.groupby("JobRole").size()

# Employees who left in each job role
jobrole_left = (
    df[df["Attrition"] == "Yes"]
    .groupby("JobRole")
    .size()
)

# Calculate attrition rate
jobrole_attrition_rate = (
    jobrole_left / jobrole_total * 100
).fillna(0).sort_values(ascending=False)

# Display results
print("\nJob Role-wise Attrition Rate (%)")
print("----------------------------------")
print(jobrole_attrition_rate.round(2))

# Create chart
ax = jobrole_attrition_rate.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Job Role-wise Employee Attrition Rate")
plt.xlabel("Job Role")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=45, ha="right")

# Add labels
for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%", padding=3)

plt.tight_layout()

# Save chart
OUTPUT_FILE = REPORTS_DIR / "jobrole_attrition_rate.png"
plt.savefig(OUTPUT_FILE, dpi=300)

print("\nChart saved successfully:")
print(OUTPUT_FILE)

plt.show()