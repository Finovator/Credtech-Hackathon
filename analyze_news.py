import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

try:
    # Load cleaned news
    df = pd.read_csv("data/cleaned_news.csv", encoding="utf-8")

    # Init VADER
    analyzer = SentimentIntensityAnalyzer()

    # Apply sentiment on description
    df["sentiment_score"] = df["description"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

    # Save result
    df.to_csv("data/news_with_sentiment.csv", index=False, encoding="utf-8")

    print("✅ Sentiment analysis done. Saved to data/news_with_sentiment.csv")
    print(df.head())

except Exception as e:
    print("⚠️ Error while analyzing sentiment:", e)
