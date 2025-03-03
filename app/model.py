import joblib
import os
import numpy as np

MODEL_PATH = os.getenv('MODEL_PATH', 'model.joblib')

def train(X, y):
    """Train a simple model and save it."""
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def predict(features):
    """Make a prediction using the saved model."""
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        return model.predict([features])[0].tolist()
    return "Model not trained yet"