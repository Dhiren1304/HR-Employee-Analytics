
import pandas as pd

# Load the dataset
df = pd.read_csv(
    "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# 1. Check missing values
print("MISSING VALUES")
print(df.isnull().sum())

# 2. Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# 3. Check unique values in each column
print("\nUNIQUE VALUES")
print(df.nunique().sort_values())

# 4. Check categorical columns
print("\nDEPARTMENT VALUES")
print(df["Department"].value_counts())

print("\nATTRITION VALUES")
print(df["Attrition"].value_counts())

print("\nOVERTIME VALUES")
print(df["OverTime"].value_counts())