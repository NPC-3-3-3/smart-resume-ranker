from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from model.ranker import ResumeRanker
from utils.parser import ResumeParser
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Initialize components
ranker = ResumeRanker()
parser = ResumeParser()

# Store ranking history
ranking_history = []

@app.route('/api/job-description', methods=['POST'])
def save_job_description():
    try:
        data = request.get_json()
        job_desc = data.get('description', '')
        # Store job description for ranking context
        global current_job_description
        current_job_description = job_desc
        return jsonify({'message': 'Job description saved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

current_job_description = ''

@app.route('/api/rank-resume', methods=['POST'])
def rank_resume():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Save uploaded file temporarily
        temp_path = f"temp_{file.filename}"
        file.save(temp_path)

        # Parse resume content
        if file.filename.lower().endswith('.txt'):
            resume_text = parser.parse_text_file(temp_path)
        elif file.filename.lower().endswith('.pdf'):
            resume_text = parser.parse_pdf_file(temp_path)
        else:
            os.remove(temp_path)
            return jsonify({'error': 'Unsupported file format. Use .txt or .pdf'}), 400

        # Clean up temp file
        os.remove(temp_path)

        if resume_text.startswith("Error"):
            return jsonify({'error': resume_text}), 400

        # Rank the resume
        result = ranker.rank_resume(resume_text)

        # Extract additional info
        skills = parser.extract_skills(resume_text)
        experience_years = parser.extract_experience_years(resume_text)

        # Store in history
        history_entry = {
            'filename': file.filename,
            'score': result.get('score', 0),
            'rank': result.get('rank', 'Unknown'),
            'skills': skills,
            'experience_years': experience_years,
            'timestamp': datetime.now().isoformat()
        }
        ranking_history.append(history_entry)

        # Keep only last 100 entries
        if len(ranking_history) > 100:
            ranking_history.pop(0)

        response = {
            'score': result.get('score', 0),
            'rank': result.get('rank', 'Unknown'),
            'skills': skills,
            'experience_years': experience_years,
            'filename': file.filename
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify(ranking_history[-10:])  # Return last 10 entries

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    if not ranking_history:
        return jsonify({
            'total_rankings': 0,
            'average_score': 0,
            'rank_distribution': {}
        })

    scores = [entry['score'] for entry in ranking_history]
    ranks = [entry['rank'] for entry in ranking_history]

    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    return jsonify({
        'total_rankings': len(ranking_history),
        'average_score': round(sum(scores) / len(scores), 2),
        'rank_distribution': rank_counts
    })

@app.route('/api/templates', methods=['GET'])
def get_templates():
    try:
        with open('frontend/resume_templates.json', 'r') as f:
            templates = json.load(f)
        return jsonify(templates)
    except FileNotFoundError:
        return jsonify({'error': 'Templates file not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
