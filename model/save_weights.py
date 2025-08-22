import json

weights = {
    "price_weight": 0.20,
    "volatility_weight": 0.20,
    "gdp_weight": 0.30,
    "unemployment_weight": 0.20,
    "sentiment_weight": 0.10
}

with open("model/model_weights.json", "w") as f:
    json.dump(weights, f)

