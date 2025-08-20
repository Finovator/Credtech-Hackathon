import pandas as pd

try:
    # Load raw news
    df = pd.read_csv("data/news.csv")

    print("Before cleaning:")
    print(df.info())

    # Remove duplicates
    df = df.drop_duplicates(subset=["company", "title"])

    # Handle missing values
    df["description"] = df["description"].fillna("No description")
    df = df.dropna(subset=["title", "publishedAt"])  # title/date must exist

    # Convert date to YYYY-MM-DD
    df["publishedAt"] = pd.to_datetime(df["publishedAt"], errors="coerce").dt.strftime("%Y-%m-%d")
    df = df.dropna(subset=["publishedAt"])

    # Map company names to tickers
    company_map = {
        "Apple": "AAPL",
        "Tesla": "TSLA",
        "Amazon": "AMZN",
        "Microsoft": "MSFT",
        "Walmart": "WMT"
    }
    df["company"] = df["company"].map(company_map)

    # Save cleaned data
    df.to_csv("data/cleaned_news.csv", index=False, encoding="utf-8")

    print("\n✅ Cleaned data saved to data/cleaned_news.csv")
    print(df.head())

except Exception as e:
    print("⚠️ Error while cleaning news:", e)
