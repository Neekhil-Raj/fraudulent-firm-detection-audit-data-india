```markdown
# 🕵️ Fraudulent Firm Detection Using Audit Data (India, 2015–2016)

## 📌 Overview

This project focuses on building a machine learning classification model to identify potentially **fraudulent firms** using one year of non-confidential audit data (2015–2016) sourced from the **Auditor Office of India**. The model is designed to support government auditors in identifying high-risk entities across various public and private sectors.

---

## 📊 Dataset Description

The dataset includes audit records of firms spanning multiple sectors, with each record containing features extracted from:

- Historical audit data  
- Audit-paras (noted irregularities)  
- Environmental compliance reports  
- Firm reputation summaries  
- Ongoing issues and legal reports  
- Financial indicators (profit/loss)  
- Follow-up and re-audit findings

These features were shortlisted based on expert interviews with auditors, and their presence was estimated using historical and current audit records.

### 🔢 Sector-Wise Distribution of Firms

| Sector                 | Number of Firms |
|------------------------|-----------------|
| Agriculture            | 200             |
| Irrigation             | 114             |
| Animal Husbandry       | 95              |
| Buildings and Roads    | 82              |
| Public Health          | 77              |
| Forest                 | 70              |
| Corporate              | 47              |
| Fisheries              | 41              |
| Industries             | 37              |
| Electrical             | 4               |
| Land                   | 5               |
| Science & Technology   | 3               |
| Communication          | 1               |
| Tourism                | 1               |

---

## 🧠 Problem Statement

> **Given the features extracted from an audit report, predict whether a firm is fraudulent or not.**

This is a **binary classification** task, where the model outputs `fraudulent` or `non-fraudulent` based on risk factors.

---

## ⚙️ Project Structure

```
```
audit_risk_classifier/
├── data/
│   └── risk_factors.csv
├── notebooks/
│   └── exploratory_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── visualize.py
│   ├── model.py
│   └── utils.py
├── results/
│   └── feature_importance.csv
├── main.py
├── requirements.txt
└── README.md


````

---

## 🔍 Approach

1. **Data Preprocessing**
   - Handling missing values
   - Encoding categorical features
   - Feature selection based on correlation and importance

2. **Exploratory Data Analysis (EDA)**
   - Sector-wise fraud distribution
   - Risk factor visualization
   - Class imbalance check

3. **Modeling**
   - Logistic Regression
   - Random Forest
   - XGBoost
   - Evaluation with metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC

4. **Interpretability**
   - Feature importance analysis
   - SHAP value-based explanation

---

## 📈 Results

- Best model: `Random Forest`
- ROC-AUC: `0.92`
- F1-Score: `0.88`
- Key features influencing prediction:
  - Prior audit-paras
  - Loss-value records
  - Firm reputation score
  - Ongoing issue reports

---

## 🧰 Tech Stack

- **Language**: Python 3.x  
- **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn, SHAP  
- **Environment**: Jupyter Notebook, Google Colab

---

## 📎 Installation

```bash
git clone https://github.com/Neekhil-Raj/fraudulent-firm-detection-audit-data-india
cd fraudulent-firm-detection-audit-data-india
pip install -r requirements.txt
````

---

## 🚀 Future Enhancements

* Incorporate time-series risk trends
* Experiment with ensemble models and deep learning
* Add real-time flagging API for auditor usage
