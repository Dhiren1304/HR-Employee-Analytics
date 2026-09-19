
import pandas as pd

# Load the dataset
df = pd.read_csv(
    "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

print("========== CONSTANT COLUMNS ==========")

# Find columns with only one unique value
constant_columns = df.columns[df.nunique() == 1].tolist()

print(constant_columns)


print("\n========== CONSTANT COLUMN VALUES ==========")

# Display the actual values
for column in constant_columns:
    print(column, ":", df[column].unique())


print("\n========== NUMERICAL DATA SUMMARY ==========")

# Summary statistics for numerical columns
print(df.describe().T)


print("\n========== CATEGORY INSPECTION ==========")

# Display unique values in important categorical columns
categorical_columns = [
    "Department",
    "JobRole",
    "BusinessTravel",
    "EducationField",
    "MaritalStatus",
    "Gender",
    "OverTime",
    "Attrition"
]

for column in categorical_columns:
    print(f"\n{column}")
    print(df[column].unique())


print("\n========== RANGE VALIDATION ==========")

# Check selected numerical columns for negative values
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    negative_count = (df[column] < 0).sum()

    if negative_count > 0:
        print(column, "has", negative_count, "negative values")

print("Range validation completed.")