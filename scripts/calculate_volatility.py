import pandas as pd
# Load cleaned stocks
df = pd.read_csv("data/cleaned_stocks.csv")
# Calculate 5-day rolling volatility per company
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["company", "date"])
df["volatility"] = df.groupby("company")["change"].rolling(window=5, min_periods=1).std().reset_index(drop=True)
df["volatility"] = df["volatility"].fillna(0)
# Save with volatility
df.to_csv("data/stocks_with_volatility.csv", index=False)
print("Stocks with volatility:\n", df.head(10))
