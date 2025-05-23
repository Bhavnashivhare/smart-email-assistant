import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from utils.preprocess import clean_text

# Load dataset
df = pd.read_csv("data/emails.csv")

# Clean text
df["clean_text"] = df["email_text"].apply(clean_text)

# Features and labels
X = df["clean_text"]
y = df["category"]

# Vectorize
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

# Train model
model = RandomForestClassifier()
model.fit(X_vect, y)

# Save model and vectorizer
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model and vectorizer saved.")