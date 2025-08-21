import pandas as pd

try:
    # Load sentiment data
    df = pd.read_csv("data/news_with_sentiment.csv")

    # Define sentiment categories
    def label_sentiment(score):
        if score >= 0.05:
            return "positive"
        elif score <= -0.05:
            return "negative"
        else:
            return "neutral"

    df["sentiment_label"] = df["sentiment_score"].apply(label_sentiment)

    # Company-wise summary
    summary = df.groupby("company").agg(
        avg_sentiment=("sentiment_score", "mean"),
        positive_count=("sentiment_label", lambda x: (x == "positive").sum()),
        negative_count=("sentiment_label", lambda x: (x == "negative").sum()),
        neutral_count=("sentiment_label", lambda x: (x == "neutral").sum()),
        total_articles=("sentiment_label", "count")
    ).reset_index()

    # Save summary
    summary.to_csv("data/sentiment_summary.csv", index=False, encoding="utf-8")

    print("✅ Sentiment summary created → data/sentiment_summary.csv")
    print(summary)

except Exception as e:
    print("⚠️ Error while summarizing sentiment:", e)
