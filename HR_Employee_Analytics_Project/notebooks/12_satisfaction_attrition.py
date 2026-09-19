
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

# Calculate total employees by job satisfaction
satisfaction_total = df.groupby(
    "JobSatisfaction"
).size()

# Calculate employees who left
satisfaction_left = (
    df[df["Attrition"] == "Yes"]
    .groupby("JobSatisfaction")
    .size()
)

# Calculate attrition rate
satisfaction_attrition_rate = (
    satisfaction_left / satisfaction_total * 100
).fillna(0)

# Ensure all satisfaction levels appear
satisfaction_attrition_rate = (
    satisfaction_attrition_rate.reindex(
        [1, 2, 3, 4],
        fill_value=0
    )
)

# Display results
print("\nJob Satisfaction-wise Attrition Rate (%)")
print("------------------------------------------")
print(satisfaction_attrition_rate.round(2))

# Create chart
ax = satisfaction_attrition_rate.plot(
    kind="bar",
    figsize=(9, 6)
)

plt.title("Job Satisfaction vs Employee Attrition")
plt.xlabel("Job Satisfaction Rating")
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
OUTPUT_FILE = REPORTS_DIR / "satisfaction_attrition_rate.png"
plt.savefig(OUTPUT_FILE, dpi=300)

print("\nChart saved successfully:")
print(OUTPUT_FILE)

plt.show()