import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from src.data_loader import load_data
from src.preprocess import handle_missing_values, drop_columns
from src.visualize import plot_risk_distribution, correlation_plot
from src.model import fit_and_evaluate
from src.utils import get_important_features

# Load and preprocess data
df = load_data("data\Audit_firm_risk_factors.csv")
df = handle_missing_values(df)

# Visualizations
plot_risk_distribution(df)
correlation_plot(df)

# Drop unwanted columns
df = drop_columns(df, ['TOTAL'])

# Train-test split
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

# Train model
dt = DecisionTreeClassifier(random_state=1)
metrics = fit_and_evaluate(dt, X_train, X_test, y_train, y_test)

# Print metrics
result = pd.DataFrame(columns=['score', 'recall', 'precision', 'specificity', 'f1_score'])
result.loc['Decision Tree'] = metrics
print(result)

# Important features
important_features, feature_importances_df = get_important_features(dt, X_train)
feature_importances_df.to_csv('results/feature_importance.csv', index=False)

# Retrain with important features
X_imp = df[important_features]
X_train, X_test, y_train, y_test = train_test_split(X_imp, y, stratify=y, random_state=1)
metrics_important = fit_and_evaluate(dt, X_train, X_test, y_train, y_test)
result.loc['Decision Tree (important features)'] = metrics_important
print(result)
