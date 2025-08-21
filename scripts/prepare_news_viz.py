import pandas as pd

try:
    # Load sentiment data
    df = pd.read_csv("data/news_with_sentiment.csv")

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Create week column
    df["week"] = df["date"].dt.to_period("W").dt.start_time

    # Aggregate sentiment by company & week
    viz_df = df.groupby(["company", "week"]).agg({
    "sentiment_score": "mean"
    }).reset_index()

    viz_df.rename(columns={"sentiment_score": "sentiment"}, inplace=True)

    # Save output
    viz_df.to_csv("data/news_viz.csv", index=False)
    print("✅ Created news_viz.csv")
    print(viz_df.head())

except Exception as e:
    print("❌ Error:", e)
