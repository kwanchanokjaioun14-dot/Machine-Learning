import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv("fifa.csv")

# ----------------------------
# Label Encoding
# ----------------------------
le = LabelEncoder()

df["preferred_foot"] = le.fit_transform(df["preferred_foot"])

print("===== Label Encoding =====")
print(df[["preferred_foot"]].head())

# ----------------------------
# One-Hot Encoding
# ----------------------------
df = pd.get_dummies(df, columns=["position"])

print("\n===== One-Hot Encoding =====")
print(df.head())

print("\nShape After Encoding:", df.shape)