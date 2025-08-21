import pandas as pd

try:
    # Load news data with sentiment scores
    print("📊 Preparing news visualization data...")
    df = pd.read_csv("data/news_with_sentiment.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["week"] = df["date"].dt.to_period("W").dt.start_time

    viz_df = df.groupby(["company", "week"]).agg({
        "sentiment_score": "mean"
    }).reset_index()

    # Rename to cleaner column name
    viz_df.rename(columns={"sentiment_score": "sentiment"}, inplace=True)

    viz_df.to_csv("data/news_viz.csv", index=False)
    print("✅ News visualization data saved to data/news_viz.csv")
    print(viz_df.head(10))

except Exception as e:
    print("❌ Error preparing news viz data:", e)
    print("⚠️ Error while preparing news visualization data:", e)