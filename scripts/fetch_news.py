import requests
import pandas as pd

# 🔑 Replace with your actual NewsAPI key
API_KEY = "55bc257d219742faaeb6d49001d68576"

companies = ["Apple", "Tesla", "Amazon", "Microsoft", "Walmart"]
all_articles = []

for company in companies:
    print(f"\nFetching news for {company}...")  # debug log
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # 👇 DEBUG: print whole API response to see what’s happening
    print("API response sample:", data.get("status"), "| totalResults:", data.get("totalResults"))

    if data.get("status") == "ok":
        for article in data["articles"][:5]:
            all_articles.append({
                "company": company,
                "title": article["title"],
                "description": article["description"],
                "publishedAt": article["publishedAt"],
                "url": article["url"]
            })
    else:
        print("⚠️ Error fetching:", data)

# Save to CSV
df = pd.DataFrame(all_articles)
df.to_csv("data/news.csv", index=False, encoding="utf-8")

print("\n✅ Finished. Articles saved:", len(all_articles))

