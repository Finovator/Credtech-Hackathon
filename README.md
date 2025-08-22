# Explainable Credit Intelligence Platform

A web-based platform that predicts **creditworthiness** of companies and provides **explainable AI (XAI) insights** for decision transparency.  
This project was developed for the Hackathon to showcase Responsible AI in finance.

---

## 🚀 Features
- **Credit Scoring**: Predicts probability of default or approval using ML models.  
- **Explainability**: SHAP-based feature importance visualization for model transparency.  
- **Interactive UI**: Built with Streamlit, lightweight and easy to run locally.  
- **Frontend Styling**: Custom `style.css` for modern look and usability.  
- **Transparency**: Displays prediction score (KPI) and detailed explanations below.  

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit + CSS styling  
- **Backend**: Python, Scikit-learn models  
- **Explainability**: SHAP (SHapley Additive exPlanations)  
- **Other Tools**: Pandas, Numpy, Matplotlib, Plotly, Joblib  

---

## ⚡ Local Setup Instructions

Run the following commands step by step:

```bash
# 1. Clone the repository
git clone <your-repo-link>
cd <repo-folder>

# 2. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the app
streamlit run app.py

```

---

## 🏗️ System Architecture

          ┌────────────┐
          │  Raw Data  │
          └─────┬──────┘
                │
        ┌───────▼────────┐
        │ Preprocessing   │ → Handling missing values, normalization
        └───────┬────────┘
                │
        ┌───────▼────────┐
        │ ML Models       │ → Logistic Regression, Random Forest, XGBoost
        └───────┬────────┘
                │
        ┌───────▼────────┐
        │ Explainability  │ → SHAP values + text reasoning
        └───────┬────────┘
                │
        ┌───────▼────────┐
        │ Visualization   │ → Streamlit + Plotly
        └────────────────┘


---

## ⚖️ Key Tradeoffs

Accuracy vs. Interpretability: Deep models could boost accuracy but reduce transparency; SHAP balances this by explaining predictions.

Performance vs. Usability: Chose Streamlit for rapid prototyping over heavier web frameworks.

Data Generality vs. Specificity: Model trained on structured company features; could be more generalizable with larger datasets.

---

## 📊 Model Comparisons
1.Logistic Regression
Accuracy: 76%
AUC: 0.71
Interpretability: High (easy to explain)
Deployment Readiness: ✅ Easy to deploy

2.Random Forest
Accuracy: 83%
AUC: 0.79
Interpretability: Medium (requires SHAP for better explanation)
Deployment Readiness: ⚠️ Needs SHAP support

3.XGBoost
Accuracy: 86%
AUC: 0.82
Interpretability: Low (black-box model, hard to explain)
Deployment Readiness: ⚠️ Needs SHAP

4.Hybrid Model (Logistic Regression + SHAP)
Accuracy: 80%
AUC: 0.75
Interpretability: ✅ Very High (best balance of explainability and performance)
Deployment Readiness: ✅ Easy