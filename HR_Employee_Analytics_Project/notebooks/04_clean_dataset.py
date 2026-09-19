
import pandas as pd

# Load raw dataset
df = pd.read_csv(
    "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

print("ORIGINAL DATASET SHAPE:", df.shape)

# Create a copy for cleaning
cleaned_df = df.copy()

# Identify constant columns
constant_columns = cleaned_df.columns[
    cleaned_df.nunique() == 1
].tolist()

print("\nCONSTANT COLUMNS:")
print(constant_columns)

# Remove constant columns
cleaned_df = cleaned_df.drop(
    columns=constant_columns
)

print("\nCLEANED DATASET SHAPE:", cleaned_df.shape)

# Check EmployeeNumber uniqueness
print("\nEMPLOYEE NUMBER UNIQUENESS:")
print(
    cleaned_df["EmployeeNumber"].nunique(),
    "unique values out of",
    len(cleaned_df)
)

# Save cleaned dataset
cleaned_df.to_csv(
    "../processed/hr_employee_cleaned.csv",
    index=False
)

print("\nCLEANED DATASET SAVED SUCCESSFULLY")