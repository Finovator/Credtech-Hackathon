import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/sentiment_summary.csv")

# 1. Bar chart of average sentiment
plt.figure(figsize=(8,5))
plt.bar(df["company"], df["avg_sentiment"], color="skyblue")
plt.title("Average Sentiment per Company")
plt.xlabel("Company")
plt.ylabel("Average Sentiment Score")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("data/avg_sentiment.png")
plt.close()

# 2. Stacked bar chart of sentiment counts
plt.figure(figsize=(10,6))
plt.bar(df["company"], df["positive_count"], label="Positive", color="green")
plt.bar(df["company"], df["neutral_count"], bottom=df["positive_count"], label="Neutral", color="gray")
plt.bar(df["company"], df["negative_count"], 
        bottom=df["positive_count"]+df["neutral_count"], 
        label="Negative", color="red")
plt.title("Sentiment Distribution per Company")
plt.xlabel("Company")
plt.ylabel("Number of Articles")
plt.legend()
plt.savefig("data/sentiment_distribution.png")
plt.close()

# 3. Pie chart of overall sentiment
total_pos = df["positive_count"].sum()
total_neg = df["negative_count"].sum()
total_neu = df["neutral_count"].sum()

plt.figure(figsize=(6,6))
plt.pie([total_pos, total_neu, total_neg], 
        labels=["Positive", "Neutral", "Negative"], 
        autopct="%1.1f%%", colors=["green","gray","red"], startangle=140)
plt.title("Overall Sentiment Distribution (All Companies)")
plt.savefig("data/overall_sentiment_pie.png")
plt.close()

print("✅ Visualization saved: avg_sentiment.png, sentiment_distribution.png, overall_sentiment_pie.png")
