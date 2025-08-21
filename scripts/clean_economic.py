import pandas as pd
from pathlib import Path

RAW = Path("data/economic.csv")
OUT = Path("data/cleaned_economic.csv")

try:
    if not RAW.exists():
        raise FileNotFoundError(f"Missing {RAW}. Run fetch_economic.py first.")

    df = pd.read_csv(RAW)
    # Keep only what we need
    if "date" not in df or "value" not in df:
        raise KeyError("Input must have 'date' and 'value' columns.")

    # Make numeric, drop non-numeric/null, keep positives
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    df = df[df["value"] > 0]

    # Standardize date format YYYY-MM-DD
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    # Optional: sort & drop duplicates
    df = df.sort_values("date").drop_duplicates(subset=["date"], keep="last")

    df.to_csv(OUT, index=False)
    print(f"OK → wrote {OUT} ({len(df)} rows)")
    print(df)
except Exception as e:
    print("Error cleaning GDP:", e)
