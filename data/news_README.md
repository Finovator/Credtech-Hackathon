# News Data Pipeline

## Overview
This pipeline fetches, cleans, analyzes, and summarizes news headlines for 5 companies (AAPL, TSLA, AMZN, MSFT, WMT).

## Files
- `news.csv`: Raw headlines from NewsAPI.
- `cleaned_news.csv`: Cleaned data (no duplicates, valid dates).
- `news_with_sentiment.csv`: Headlines with sentiment scores.
- `news_viz.csv`: Weekly average sentiment per company.

## Scripts
- `fetch_news.py`: Fetches news via NewsAPI.
- `clean_news.py`: Cleans raw headlines.
- `analyze_news.py`: Adds sentiment scores.
- `prepare_news_viz.py`: Aggregates weekly average sentiment.

## Dependencies
- pandas
- requests
- textblob
