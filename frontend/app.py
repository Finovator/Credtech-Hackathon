import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page setup ---
st.set_page_config(page_title="Explainable Credit Intelligence Platform", layout="wide")
st.title("💡 Explainable Credit Intelligence Platform")

# --- Load data ---
@st.cache_data
def load_data():
    viz_df = pd.read_csv("data/viz_data.csv")
    news_viz_df = pd.read_csv("data/news_viz.csv")
    scores_df = pd.read_csv("data/scores.csv")
    return viz_df, news_viz_df, scores_df

viz_df, news_viz_df, scores_df = load_data()

# --- Sidebar company selector ---
companies = viz_df["company"].unique().tolist()
company = st.sidebar.selectbox("🏢 Select Company", companies)

# --- Latest score (KPI card) ---
latest_score = None
if "score" in scores_df.columns:
    company_scores = scores_df[scores_df["company"] == company]
    if not company_scores.empty:
        latest_score = company_scores.iloc[-1]["score"]

if latest_score is not None:
    st.metric(label=f"📌 Latest Credit Score for {company}", value=round(latest_score, 2))
else:
    st.info("No credit score available for this company.")

st.subheader(f"📈 Overview for {company}")

# --- Basic stats ---
stats = viz_df[viz_df["company"] == company]
st.write("### Average Metrics")
st.dataframe(stats.set_index("company"))

# --- Price trend ---
st.write("### Price Trend")
if "date" in scores_df.columns and "score" in scores_df.columns:
    fig_price = px.line(
        scores_df[scores_df["company"] == company],
        x="date", y="score",
        title=f"{company} Score Trend"
    )
else:
    fig_price = px.line(
        viz_df[viz_df["company"] == company],
        x="data_points", y="price",
        title=f"{company} Price vs Data Points"
    )
st.plotly_chart(fig_price, use_container_width=True)

# --- Sentiment trend ---
st.write("### News Sentiment Over Time")
if "week" in news_viz_df.columns:
    fig_sent = px.line(
        news_viz_df[news_viz_df["company"] == company],
        x="week", y="sentiment",
        title=f"{company} Weekly Sentiment"
    )
else:
    fig_sent = px.line(
        news_viz_df[news_viz_df["company"] == company],
        x="data_points", y="sentiment",
        title=f"{company} Sentiment (avg)"
    )
st.plotly_chart(fig_sent, use_container_width=True)

# --- Explainability Section ---
st.write("### 🔍 Explainability")
if "explanation" in scores_df.columns:
    latest = scores_df[scores_df["company"] == company].tail(5)
    st.dataframe(latest[["date", "score", "explanation"]])
else:
    st.info("No detailed explanations available in the data.")
