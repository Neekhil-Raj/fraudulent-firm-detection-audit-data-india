import pandas as pd

def get_important_features(model, X_train, threshold=0.1):
    feature_importances = pd.DataFrame({
        'features': X_train.columns,
        'Importance': model.feature_importances_
    })

    important = feature_importances[feature_importances['Importance'] > threshold]['features'].tolist()
    return important, feature_importances
