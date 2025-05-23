import joblib
import os
import numpy as np
from utils.preprocess import clean_text

class EmailClassifier:
    def __init__(self):
        model_path = os.path.join("models", "classifier.pkl")
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(os.path.join("models", "vectorizer.pkl"))

    def predict(self, email_text):
        clean = clean_text(email_text)
        vector = self.vectorizer.transform([clean])
        prediction = self.model.predict(vector)[0]
        confidence = np.max(self.model.predict_proba(vector))
        return {
            "email_text": email_text,
            "predicted_category": prediction,
            "confidence": round(confidence, 2)
        }