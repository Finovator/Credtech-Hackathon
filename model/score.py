import pandas as pd

try:
    df = pd.read_csv("data/model_data.csv")
    # Debug: Print data info
    print("df info:\n", df.info())
    print("df head:\n", df.head())

    # Normalize features (0 to 1), handle zero range
    price_range = df["price"].max() - df["price"].min()
    df["price_norm"] = (df["price"] - df["price"].min()) / price_range if price_range > 0 else 0
    volatility_range = df["volatility"].max() - df["volatility"].min()
    df["volatility_norm"] = 1 - (df["volatility"] - df["volatility"].min()) / volatility_range if volatility_range > 0 else 0
    gdp_range = df["gdp"].max() - df["gdp"].min()
    df["gdp_norm"] = (df["gdp"] - df["gdp"].min()) / gdp_range if gdp_range > 0 else 0
    unemployment_range = df["unemployment_rate"].max() - df["unemployment_rate"].min()
    df["unemployment_norm"] = 1 - (df["unemployment_rate"] - df["unemployment_rate"].min()) / unemployment_range if unemployment_range > 0 else 0
    df["sentiment_norm"] = (df["sentiment"] + 1) / 2  # Scale -1 to 1 -> 0 to 1

    # Debug: Print normalized values
    print("Normalized values head:\n", df[["price_norm", "volatility_norm", "gdp_norm", "unemployment_norm", "sentiment_norm"]].head())

    # Weighted average score
    df["score"] = (
        0.20 * df["price_norm"] +
        0.20 * df["volatility_norm"] +
        0.30 * df["gdp_norm"] +
        0.20 * df["unemployment_norm"] +
        0.10 * df["sentiment_norm"]
    ) * 100

    df[["company", "date", "score"]].to_csv("data/scores.csv", index=False)
    print("Scores:\n", df[["company", "date", "score"]].head(10))
except Exception as e:
    print("Error in scoring:", e)