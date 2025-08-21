import requests
import pandas as pd

FRED_API_KEY = "ff99bc86366768d3051b0be41e59f14b"   # paste your key
series_id = "GDPC1"   # U.S. Real GDP

url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"

try:
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data["observations"])
    df = df[["date", "value"]] 
    df.to_csv("economic.csv", index=False)
    print(df)
except Exception as e:
    print("Error:", e)
