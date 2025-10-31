import joblib
import numpy as np

class ResumeRanker:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.load_model()

    def load_model(self):
        try:
            self.model = joblib.load('backend/model/resume_ranker.pkl')
            self.vectorizer = joblib.load('backend/model/vectorizer.pkl')
            print("Model loaded successfully!")
        except FileNotFoundError:
            print("Model files not found. Please train the model first.")
            return False
        return True

    def rank_resume(self, resume_text):
        if self.model is None:
            return {"error": "Model not loaded"}

        # Vectorize the resume text
        resume_vec = self.vectorizer.transform([resume_text])

        # Predict score
        score = self.model.predict(resume_vec)[0]

        # Ensure score is between 0 and 10
        score = max(0, min(10, score))

        return {
            "score": round(float(score), 2),
            "rank": self.get_rank_category(score)
        }

    def get_rank_category(self, score):
        if score >= 8:
            return "Excellent"
        elif score >= 6:
            return "Good"
        elif score >= 4:
            return "Average"
        else:
            return "Below Average"
