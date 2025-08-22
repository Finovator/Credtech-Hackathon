import pandas as pd

try:
    combined_df = pd.read_csv("data/combined_data.csv")
    news_df = pd.read_csv("data/news_with_sentiment.csv", usecols=["company", "date", "sentiment_score"])
    combined_df["date"] = pd.to_datetime(combined_df["date"])
    news_df["date"] = pd.to_datetime(news_df["date"])

    # Debug: Print date ranges
    print("combined_df date range:", combined_df["date"].min(), "to", combined_df["date"].max())
    print("news_df date range:", news_df["date"].min(), "to", news_df["date"].max())

    model_df = pd.merge_asof(
        combined_df.sort_values("date"),
        news_df.sort_values("date"),
        on="date",
        by="company",
        direction="nearest",
        tolerance=pd.Timedelta(days=30)  # Increased tolerance
    )
    # Debug: Print merged data sample
    print("model_df head after merge:\n", model_df[["company", "date", "sentiment_score"]].head(10))

    # Select columns and rename sentiment_score to sentiment
    model_df = model_df[["company", "date", "price", "volatility", "gdp", "unemployment_rate", "sentiment_score"]]
    model_df = model_df.rename(columns={"sentiment_score": "sentiment"})
    model_df = model_df.fillna({"sentiment": 0})
    model_df.to_csv("data/model_data.csv", index=False)
    print("Model data:\n", model_df.head(10))
except Exception as e:
    print("Error preparing model data:", e)