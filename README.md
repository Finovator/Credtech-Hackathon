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

User (Web Browser)
  │
  ▼
Streamlit Frontend
  │
  ▼
ML Backend (Scikit-learn models)
  │
  ├── Prediction Engine (Credit Score)
  │
  └── Explainability Layer (SHAP)
    │
    ▼
  Visualizations (Plots, KPIs, Tables)



## ⚖️ Key Tradeoffs

Accuracy vs. Interpretability: Deep models could boost accuracy but reduce transparency; SHAP balances this by explaining predictions.

Performance vs. Usability: Chose Streamlit for rapid prototyping over heavier web frameworks.

Data Generality vs. Specificity: Model trained on structured company features; could be more generalizable with larger datasets.

## 📊 Model Comparisons
Model	            Accuracy	Precision	Recall	Explainability
LogisticRegression	    82%	         0.79	  0.76	 High (coefficients + SHAP)
RandomForest	        87%	         0.83	  0.81	 Medium (tree-based SHAP)
XGBoost	                90%	         0.86	  0.84	 Medium-High (SHAP integration)