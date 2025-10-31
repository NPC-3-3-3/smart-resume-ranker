from flask import Flask, request, jsonify
from flask_cors import CORS
from model.ranker import ResumeRanker
from utils.parser import ResumeParser
import os
import tempfile
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Initialize components
ranker = ResumeRanker()
parser = ResumeParser()

# In-memory storage for history and statistics
ranking_history = []
statistics = {
    'total_rankings': 0,
    'average_score': 0.0,
    'total_score_sum': 0.0
}

@app.route('/api/rank-resume', methods=['POST'])
def rank_resume():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            file.save(temp_file.name)
            temp_path = temp_file.name

        try:
            # Parse file based on extension
            if file.filename.lower().endswith('.pdf'):
                resume_text = parser.parse_pdf_file(temp_path)
            elif file.filename.lower().endswith('.txt'):
                resume_text = parser.parse_text_file(temp_path)
            else:
                return jsonify({'error': 'Unsupported file type. Please upload .txt or .pdf files'}), 400

            # Extract additional information
            skills = parser.extract_skills(resume_text)
            experience_years = parser.extract_experience_years(resume_text)

            # Rank the resume
            result = ranker.rank_resume(resume_text)

            # Update statistics
            global statistics
            statistics['total_rankings'] += 1
            statistics['total_score_sum'] += result['score']
            statistics['average_score'] = statistics['total_score_sum'] / statistics['total_rankings']

            # Add to history
            history_entry = {
                'filename': file.filename,
                'score': result['score'],
                'rank': result['rank'],
                'skills': skills,
                'experience_years': experience_years,
                'timestamp': datetime.now().isoformat()
            }
            ranking_history.append(history_entry)

            # Keep only last 100 entries
            if len(ranking_history) > 100:
                ranking_history.pop(0)

            return jsonify({
                'filename': file.filename,
                'score': result['score'],
                'rank': result['rank'],
                'skills': skills,
                'experience_years': experience_years
            })

        finally:
            # Clean up temp file
            os.unlink(temp_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    return jsonify(statistics)

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify(ranking_history[-10:])  # Return last 10 entries

@app.route('/api/templates', methods=['GET'])
def get_templates():
    templates = {
        'software_engineer': {
            'title': 'Software Engineer',
            'content': 'Experienced software engineer with 5 years in Python, Java, and web development. Led team of 3 developers on e-commerce platform. Proficient in AWS, Docker, and CI/CD pipelines. Strong background in algorithms and data structures.'
        },
        'data_scientist': {
            'title': 'Data Scientist',
            'content': 'Senior data scientist with PhD in Machine Learning. 8 years experience in Python, R, TensorFlow, PyTorch. Published 15 papers in top conferences. Expert in statistical modeling and predictive analytics.'
        },
        'marketing_manager': {
            'title': 'Marketing Manager',
            'content': 'Marketing specialist with 4 years experience in digital marketing, SEO, and content creation. Managed social media campaigns for Fortune 500 companies. Proficient in Google Analytics and marketing automation tools.'
        },
        'devops_engineer': {
            'title': 'DevOps Engineer',
            'content': 'DevOps engineer with 7 years experience in cloud infrastructure, Kubernetes, and automation. Reduced deployment time by 70% at previous company. Expert in CI/CD pipelines and infrastructure as code.'
        }
    }
    return jsonify(templates)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
