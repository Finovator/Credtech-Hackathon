import requests
import pandas as pd

# FRED API key (already provided)
FRED_API_KEY = "ff99bc86366768d3051b0be41e59f14b"
series_id = "UNRATE"  # Monthly unemployment rate

url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data["observations"])
    df = df[["date", "value"]]
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # Keep only last 10 months
    df = df.tail(10)

    # Save
    df.to_csv("data/unemployment.csv", index=False)
    print("Unemployment data:\n", df)

except Exception as e:
    print("Error fetching unemployment:", e)

