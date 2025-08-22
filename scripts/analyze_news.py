import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

try:
    # Load cleaned news
    df = pd.read_csv("data/cleaned_news.csv", encoding="utf-8")

    # Init VADER
    analyzer = SentimentIntensityAnalyzer()

    # Debug: Sample descriptions
    print("Sample descriptions:\n", df["description"].head())

    # Apply sentiment on description
    df["sentiment_score"] = df["description"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])
    print("Sample sentiment scores:\n", df[["description", "sentiment_score"]].head())

    # Save result
    df.to_csv("data/news_with_sentiment.csv", index=False, encoding="utf-8")

    print("✅ Sentiment analysis done. Saved to data/news_with_sentiment.csv")
    print(df.head())
except Exception as e:
    print("⚠️ Error while analyzing sentiment:", e)