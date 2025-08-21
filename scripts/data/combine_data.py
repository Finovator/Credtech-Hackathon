import pandas as pd

try:
    # Load data
    stocks_df = pd.read_csv("data/stocks_with_volatility.csv")
    econ_df = pd.read_csv("data/cleaned_economic.csv")
    unemp_df = pd.read_csv("data/unemployment.csv")
    news_df = pd.read_csv("data/news_with_sentiment.csv")

    # Ensure required columns exist
    required_stocks = {"company", "date", "price", "change", "volatility"}
    required_econ = {"date", "value"}
    required_unemp = {"date", "value"}
    required_news = {"company", "date", "sentiment_score"}
    if not all(col in stocks_df.columns for col in required_stocks):
        raise KeyError("stocks_with_volatility.csv missing required columns")
    if not all(col in econ_df.columns for col in required_econ):
        raise KeyError("cleaned_economic.csv missing required columns")
    if not all(col in unemp_df.columns for col in required_unemp):
        raise KeyError("unemployment.csv missing required columns")
    if not all(col in news_df.columns for col in required_news):
        raise KeyError("news_with_sentiment.csv missing required columns")

    # Convert dates
    stocks_df["date"] = pd.to_datetime(stocks_df["date"], errors="coerce")
    econ_df["date"] = pd.to_datetime(econ_df["date"], errors="coerce")
    unemp_df["date"] = pd.to_datetime(unemp_df["date"], errors="coerce")
    news_df["date"] = pd.to_datetime(news_df["date"], errors="coerce")

    # Check for invalid dates
    if stocks_df["date"].isna().any() or econ_df["date"].isna().any() or unemp_df["date"].isna().any() or news_df["date"].isna().any():
        raise ValueError("Invalid dates found in one or more datasets")

    # Merge economic data (GDP + unemployment)
    combined_econ = pd.merge_asof(
        econ_df.sort_values("date"),
        unemp_df.sort_values("date"),
        on="date",
        direction="backward"
    ).rename(columns={"value_x": "gdp", "value_y": "unemployment_rate"})

    # Merge stocks with economic data
    combined_stock_econ = pd.merge_asof(
        stocks_df.sort_values("date"),
        combined_econ.sort_values("date"),
        on="date",
        direction="backward"
    )

    # Merge with news sentiment
    combined_df = pd.merge_asof(
        combined_stock_econ.sort_values("date"),
        news_df.sort_values("date"),
        on="date",
        by="company",
        direction="backward"
    )

    # Select and rename columns
    combined_df = combined_df[["company", "date", "price", "change", "volatility", "gdp", "unemployment_rate", "sentiment_score"]]
    combined_df = combined_df.rename(columns={"sentiment_score": "sentiment"})
    combined_df["sentiment"] = combined_df["sentiment"].fillna(0)

    # Save result
    combined_df.to_csv("data/combined_data.csv", index=False)
    print("Combined data:\n", combined_df.head(10))

except Exception as e:
    print("Error combining data:", e)