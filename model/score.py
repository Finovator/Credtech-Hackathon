import pandas as pd

try:
    # Sample data for testing
    sample_df = pd.DataFrame({
        "company": ["AAPL", "TSLA"],
        "date": ["2025-07-16", "2025-07-16"],
        "price": [200.0, 150.0],
        "volatility": [0.02, 0.05]
    })
    sample_df["score"] = (sample_df["price"] / sample_df["price"].max()) * 100
    sample_df.to_csv("data/sample_scores.csv", index=False)
    print("Sample scores:\n", sample_df)
except Exception as e:
    print("Error in sample scoring:", e)