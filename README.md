# Smart Resume Ranker

An AI-powered resume analysis and ranking system that uses machine learning to evaluate resumes and provide detailed feedback.

## Features

- **AI-Powered Ranking**: Machine learning model trained on resume data to score resumes 1-10
- **Skill Extraction**: Automatically identifies technical skills and competencies
- **Experience Analysis**: Extracts years of experience from resume content
- **Web Interface**: Modern, responsive frontend for easy resume upload and analysis
- **REST API**: Backend API for programmatic access
- **Ranking History**: Track and view previous resume rankings
- **Statistics Dashboard**: View overall statistics and ranking distributions

## Project Structure

```
smart-resume-ranker/
├── backend/                 # Flask backend API
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── model/              # ML model components
│   │   └── ranker.py       # Resume ranking logic
│   └── utils/              # Utility functions
│       └── parser.py       # Resume parsing utilities
├── ml/                     # Machine learning components
│   ├── train_model.py      # Model training script
│   └── resume_dataset.csv  # Training dataset
├── frontend/               # Web frontend
│   ├── index.html          # Main web interface
│   └── resume_templates.json # Resume templates
├── test_resume1.txt        # Sample resume for testing
├── test_resume2.txt        # Sample resume for testing
└── README.md               # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd smart-resume-ranker/backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Model Training
1. Navigate to the project root:
   ```bash
   cd smart-resume-ranker
   ```

2. Train the ML model:
   ```bash
   python ml/train_model.py
   ```

### Running the Application

1. Start the backend server:
   ```bash
   python backend/app.py
   ```
   The API will be available at `http://localhost:5000`

2. Open the frontend:
   - Open `frontend/index.html` in your web browser
   - Or serve it through a local web server

## API Endpoints

### POST /api/rank-resume
Upload a resume file for analysis.

**Parameters:**
- `file`: Resume file (TXT or PDF format)

**Response:**
```json
{
  "score": 8.5,
  "rank": "Excellent",
  "skills": ["Python", "JavaScript", "React"],
  "experience_years": 4,
  "filename": "resume.txt"
}
```

### GET /api/history
Get recent ranking history.

**Response:**
```json
[
  {
    "filename": "resume.txt",
    "score": 8.5,
    "rank": "Excellent",
    "skills": ["Python", "JavaScript"],
    "experience_years": 4,
    "timestamp": "2024-01-15T10:30:00"
  }
]
```

### GET /api/statistics
Get overall ranking statistics.

**Response:**
```json
{
  "total_rankings": 25,
  "average_score": 7.2,
  "rank_distribution": {
    "Excellent": 8,
    "Good": 12,
    "Average": 4,
    "Below Average": 1
  }
}
```

## Usage

1. **Upload Resume**: Click or drag a resume file (TXT format) onto the upload area
2. **View Results**: See the AI-generated score, rank category, and extracted skills
3. **Check History**: View previous rankings in the history section
4. **Monitor Statistics**: Track overall performance metrics

## Technologies Used

- **Backend**: Flask, scikit-learn, pandas, numpy
- **Machine Learning**: TF-IDF Vectorization, Linear Regression
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Data Processing**: Pandas, NumPy

## Model Details

The ranking model uses:
- **TF-IDF Vectorization**: Converts resume text to numerical features
- **Linear Regression**: Predicts resume scores based on content
- **Training Data**: 10 sample resumes with expert-assigned scores

## Future Enhancements

- PDF parsing support
- Advanced NLP for better skill extraction
- More sophisticated ML models (neural networks)
- User authentication and resume storage
- Batch processing capabilities
- Integration with job posting analysis

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.
