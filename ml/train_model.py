import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

def train_resume_ranker():
    # Load dataset
    df = pd.read_csv('resume_dataset.csv')

    # Prepare features and target
    X = df['resume_text']
    y = df['score']

    # Text vectorization
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_vectorized = vectorizer.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model trained successfully. MSE: {mse:.4f}")

    # Save model and vectorizer
    joblib.dump(model, 'resume_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    print("Model and vectorizer saved.")

if __name__ == "__main__":
    train_resume_ranker()
