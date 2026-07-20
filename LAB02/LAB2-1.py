import pandas as pd

# Load Dataset
df = pd.read_csv("LAB02/fifa.csv")

print("="*50)
print("Shape")
print(df.shape)

print("="*50)
print("Data Types")
print(df.dtypes)

print("="*50)
print("Summary Statistics")
print(df.describe(include="all"))

print("="*50)
print("Missing Values")
print(df.isnull().sum())

print("="*50)
print("Duplicate Records")
print(df.duplicated().sum())

print("="*50)
print("Class Distribution (Position)")
print(df["position"].value_counts())