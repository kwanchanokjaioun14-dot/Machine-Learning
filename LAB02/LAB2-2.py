import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("fifa.csv")

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["age"], bins=15)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,10))

corr = df.select_dtypes(include="number").corr()

sns.heatmap(corr,
            annot=False,
            cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()