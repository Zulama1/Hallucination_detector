from sklearn.metrics import precision_recall_fscore_support

def compute_metrics(y_true, y_pred):
    p,r,f, _ = precision_recall_fscore_support(
        y_true, y_pred, average='binary'
    )
    return {"Precision" : p, "Recall":r, "F-score":f}
