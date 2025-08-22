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

    # Contributions
    df["price_contrib"] = 0.20 * df["price_norm"] * 100
    df["volatility_contrib"] = 0.20 * df["volatility_norm"] * 100
    df["gdp_contrib"] = 0.30 * df["gdp_norm"] * 100
    df["unemployment_contrib"] = 0.20 * df["unemployment_norm"] * 100
    df["sentiment_contrib"] = 0.10 * df["sentiment_norm"] * 100

    # Weighted average score (same as sum of contributions)
    df["score"] = (
        df["price_contrib"] +
        df["volatility_contrib"] +
        df["gdp_contrib"] +
        df["unemployment_contrib"] +
        df["sentiment_contrib"]
    )

    # Add explanation with exact contributions
    df["explanation"] = df.apply(
        lambda row: (
            f"Score: {row['score']:.1f}. "
            f"Price impact: {row['price_contrib']:.1f}, "
            f"Volatility impact: {row['volatility_contrib']:.1f}, "
            f"GDP impact: {row['gdp_contrib']:.1f}, "
            f"Unemployment impact: {row['unemployment_contrib']:.1f}, "
            f"Sentiment impact: {row['sentiment_contrib']:.1f}"
        ),
        axis=1
    )

    # Save results
    df[["company", "date", "score", "explanation"]].to_csv("data/scores.csv", index=False)

    print("Scores with explanations:\n", df[["company", "date", "score", "explanation"]].head(10))

except Exception as e:
    print("Error in scoring:", e)
