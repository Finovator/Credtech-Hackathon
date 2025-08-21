import yfinance as yf
import pandas as pd
companies = ["AAPL", "TSLA", "AMZN", "MSFT", "WMT"]
stock_data = []
for company in companies:
    stock = yf.Ticker(company)
    hist = stock.history(period="1mo")  # Last 30 days
    hist["change"] = hist["Close"].pct_change().fillna(0)  # Calculate daily % change
    for date, row in hist.iterrows():
        stock_data.append({
            "company": company,
            "date": date.strftime("%Y-%m-%d"),
            "price": row["Close"],
            "change": row["change"]
        })
stock_df = pd.DataFrame(stock_data)
stock_df.to_csv("data/stocks.csv", index=False)
print(stock_df) 