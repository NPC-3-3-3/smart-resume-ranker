import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

def train_resume_ranker():
    # Load dataset
    df = pd.read_csv('ml/resume_dataset.csv')

    # Prepare features and target
    X = df['resume_text']
    y = df['score']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize text
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train model
    model = LinearRegression()
    model.fit(X_train_vec, y_train)

    # Evaluate
    y_pred = model.predict(X_test_vec)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model trained successfully. MSE: {mse:.2f}")

    # Save model and vectorizer
    os.makedirs('backend/model', exist_ok=True)
    joblib.dump(model, 'backend/model/resume_ranker.pkl')
    joblib.dump(vectorizer, 'backend/model/vectorizer.pkl')

    print("Model and vectorizer saved successfully!")

if __name__ == "__main__":
    train_resume_ranker()
