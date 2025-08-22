import pandas as pd

try:
    combined_df = pd.read_csv("data/combined_data.csv")
    news_df = pd.read_csv("data/news_with_sentiment.csv", usecols=["company", "date", "sentiment_score"])
    combined_df["date"] = pd.to_datetime(combined_df["date"])
    news_df["date"] = pd.to_datetime(news_df["date"])

    # Debug: Print column names before merge
    print("combined_df columns:", combined_df.columns.tolist())
    print("news_df columns:", news_df.columns.tolist())

    model_df = pd.merge_asof(
        combined_df.sort_values("date"),
        news_df.sort_values("date"),
        on="date",
        by="company",
        direction="backward"
    )
    # Check available columns before selection
    print("model_df columns after merge:", model_df.columns.tolist())
    model_df = model_df[["company", "date", "price", "volatility", "gdp", "unemployment_rate", "sentiment"]]
    model_df = model_df.rename(columns={"sentiment_score": "sentiment"})
    model_df = model_df.fillna({"sentiment": 0})
    model_df.to_csv("data/model_data.csv", index=False)
    print("Model data:\n", model_df.head(10))
except Exception as e:
    print("Error preparing model data:", e)