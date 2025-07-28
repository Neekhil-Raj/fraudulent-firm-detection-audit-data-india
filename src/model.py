from sklearn import metrics
from sklearn.model_selection import cross_val_score

def fit_and_evaluate(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    score = round(model.score(X_test, y_test), 3)
    tn, fp, fn, tp = metrics.confusion_matrix(y_test, pred).ravel()

    recall = round(tp / (tp + fn), 3)
    precision = round(tp / (tp + fp), 3)
    specificity = round(tn / (tn + fp), 3)
    f1_score = round(2 * precision * recall / (precision + recall), 3)

    return score, recall, precision, specificity, f1_score
