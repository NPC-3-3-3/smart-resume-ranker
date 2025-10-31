import joblib
import os

class ResumeRanker:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), '../../ml/resume_model.pkl')
        vectorizer_path = os.path.join(os.path.dirname(__file__), '../../ml/vectorizer.pkl')

        if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
            raise FileNotFoundError("Model files not found. Please train the model first.")

        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def rank_resume(self, resume_text):
        # Vectorize the resume text
        resume_vectorized = self.vectorizer.transform([resume_text])

        # Predict score
        score = self.model.predict(resume_vectorized)[0]

        # Ensure score is within 0-10 range
        score = max(0, min(10, score))

        # Determine rank
        if score >= 9:
            rank = "Excellent"
        elif score >= 7:
            rank = "Good"
        elif score >= 5:
            rank = "Average"
        else:
            rank = "Poor"

        return {
            'score': round(score, 2),
            'rank': rank
        }
