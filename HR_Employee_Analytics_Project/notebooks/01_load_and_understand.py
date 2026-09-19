
import pandas as pd

# Load the HR dataset
df = pd.read_csv(
    "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Display first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Display dataset shape
print("\nDATASET SHAPE")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Display data types
print("\nDATA TYPES")
print(df.dtypes)