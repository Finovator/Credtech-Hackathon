import pandas as pd

try:
    stocks_df = pd.read_csv("data/stocks_with_volatility.csv")
    econ_df = pd.read_csv("data/cleaned_economic.csv")
    stocks_df["date"] = pd.to_datetime(stocks_df["date"])
    econ_df["date"] = pd.to_datetime(econ_df["date"])
    combined_df = pd.merge_asof(
        stocks_df.sort_values("date"),
        econ_df.sort_values("date"),
        left_on="date",
        right_on="date",
        direction="backward"
    )
    combined_df = combined_df[["company", "date", "price", "change", "volatility", "value"]]
    combined_df = combined_df.rename(columns={"value": "gdp"})
    combined_df.to_csv("data/combined_data.csv", index=False)
    print("Combined data:\n", combined_df.head(10))
except Exception as e:
    print("Error combining data:", e)