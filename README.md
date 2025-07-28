# Fraudulent Firm Detection Using Audit Data (India, 2015–2016)

## Overview

This project involves developing a machine learning classification model to detect potentially fraudulent firms using non-confidential audit data from the Auditor Office of India. The data covers the financial year 2015–2016 and includes firm-level details across multiple government and private sectors. The objective is to assist auditors in identifying high-risk companies based on key risk indicators derived from past and present audit records.

## Dataset Description

The dataset includes audit records and associated risk factors collected from firms across a wide range of sectors. Each record captures attributes that were evaluated in consultation with auditing experts. These features include:

- Historical audit data
- Audit-paras (identified issues)
- Environmental compliance reports
- Reputation scores
- Reports on ongoing legal or regulatory issues
- Profit and loss value trends
- Follow-up audit reports

These attributes were selected based on their relevance to fraud detection and the probability of their presence was estimated using both historical and current data.

### Sector-wise Distribution of Firms

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

## Problem Statement

Given the features extracted from an audit report, the task is to classify whether a firm is fraudulent or non-fraudulent. This is framed as a binary classification problem.

## Project Structure

fraudulent-firm-detection/
├── data/ # Raw and processed datasets
├── notebooks/ # EDA and model development notebooks
├── src/ # Source code for preprocessing and training
│ ├── data_preprocessing.py
│ ├── model_training.py
│ └── utils.py
├── models/ # Saved model files
├── results/ # Visualizations and output reports
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## Approach

1. **Data Preprocessing**
   - Handling missing and inconsistent values
   - Encoding categorical variables
   - Selecting relevant features based on correlation and importance

2. **Exploratory Data Analysis**
   - Sector-wise fraud statistics
   - Risk factor distributions
   - Class imbalance analysis

3. **Model Development**
   - Algorithms used: Logistic Regression, Random Forest, XGBoost
   - Evaluation metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC

4. **Model Interpretation**
   - Feature importance ranking
   - SHAP-based interpretability for explainable results

## Results

The Random Forest model provided the best performance with the following metrics:

- ROC-AUC: 0.92
- F1-Score: 0.88

Top contributing features included audit-paras, loss-value records, firm reputation, and ongoing issue reports.

## Technology Stack

- Python 3.x
- Pandas, NumPy
- Scikit-learn, XGBoost
- Matplotlib, Seaborn, SHAP
- Jupyter Notebook, Google Colab

## Future Work

Time-based modeling of fraud risk
Integration with real-time audit systems
Dashboard development for auditor usage
Ensemble or deep learning methods for improved accuracy

## Installation

To run this project locally:
```bash
git clone https://github.com/yourusername/fraudulent-firm-detection-audit-data-india.git
cd fraudulent-firm-detection-audit-data-india
pip install -r requirements.txt


