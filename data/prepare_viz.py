import pandas as pd

try:
    df = pd.read_csv("data/combined_data.csv")
    if not {"company", "date", "price", "volatility", "gdp", "unemployment_rate", "sentiment"}.issubset(df.columns):
        raise KeyError("combined_data.csv missing required columns")
    
    # Summarize: mean and count of data points per company
    viz_df = df.groupby("company").agg({
        "price": "mean",
        "volatility": "mean",
        "gdp": "mean",
        "unemployment_rate": "mean",
        "sentiment": "mean",
        "date": "count"  # Add count of data points
    }).reset_index()
    
    # Rename count column for clarity
    viz_df = viz_df.rename(columns={"date": "data_points"})
    
    # Round for readability
    viz_df = viz_df.round(2)
    
    # Save
    viz_df.to_csv("data/viz_data.csv", index=False)
    print("✅ Visualization data prepared. Saved to data/viz_data.csv")
    print(viz_df)
except Exception as e:
    print("⚠️ Error preparing viz data:", e)