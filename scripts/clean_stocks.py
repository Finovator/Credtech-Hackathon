import pandas as pd
# Load stocks.csv
df = pd.read_csv("data/stocks.csv")
# Check missing values
print("Missing values before:\n", df.isnull().sum())
# Fill missing prices (forward fill) and changes (0)
df["price"] = df["price"].ffill()
df["change"] = df["change"].fillna(0)
# Remove invalid prices (negative or zero)
df = df[df["price"] > 0]
# Ensure date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
# Save cleaned data
df.to_csv("data/cleaned_stocks.csv", index=False)
print("Cleaned stocks:\n", df.head(10))
print("Missing values after:\n", df.isnull().sum())