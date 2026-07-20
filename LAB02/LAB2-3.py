import pandas as pd

# Load Dataset
df = pd.read_csv("LAB02/fifa.csv")

print("="*50)
print("Before Cleaning")
print("Shape:", df.shape)

# -------------------------------
# 1. Missing Value Handling (Mean)
# -------------------------------
df_mean = df.copy()

numeric_columns = df_mean.select_dtypes(include="number").columns

for col in numeric_columns:
    df_mean[col] = df_mean[col].fillna(df_mean[col].mean())

print("\nMissing Values After Mean:")
print(df_mean.isnull().sum())

# -------------------------------
# 2. Missing Value Handling (Median)
# -------------------------------
df_median = df.copy()

for col in numeric_columns:
    df_median[col] = df_median[col].fillna(df_median[col].median())

print("\nMissing Values After Median:")
print(df_median.isnull().sum())

# -------------------------------
# 3. Duplicate Removal
# -------------------------------
print("\nDuplicate Records Before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate Records After:", df.duplicated().sum())
print("Shape After Removing Duplicates:", df.shape)

# -------------------------------
# 4. Incorrect Data Correction
# -------------------------------
if "age" in df.columns:
    df.loc[df["age"] < 0, "age"] = df["age"].median()
    print("\nIncorrect Data Corrected (Age)")

# -------------------------------
# 5. Data Type Conversion
# -------------------------------
print("\nData Types")
print(df.dtypes)

# -------------------------------
# Compare Mean vs Median
# -------------------------------
print("\nAge Mean   :", df_mean["age"].mean())
print("Age Median :", df_median["age"].median())