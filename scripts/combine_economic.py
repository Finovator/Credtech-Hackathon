import pandas as pd
try:
    gdp_df = pd.read_csv("data/cleaned_economic.csv")
    unemp_df = pd.read_csv("data/unemployment.csv")

    gdp_df["date"] = pd.to_datetime(gdp_df["date"])
    unemp_df["date"] = pd.to_datetime(unemp_df["date"])

    econ_df = pd.merge_asof(
        gdp_df.sort_values("date"),
        unemp_df.sort_values("date"),
        on="date",
        direction="backward"
    )

    econ_df = econ_df.rename(columns={"value_x": "gdp", "value_y": "unemployment_rate"})
    econ_df.to_csv("data/combined_economic.csv", index=False)

    print("Combined economic data:\n", econ_df)
except Exception as e:
    print("Error combining economic data:", e)
