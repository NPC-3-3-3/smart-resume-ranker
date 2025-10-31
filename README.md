# Smart Resume Ranker

An AI-powered resume analysis and ranking system that uses machine learning to evaluate resumes and provide detailed feedback.

## Features

- **Resume Analysis**: Upload PDF or text resumes for comprehensive analysis
- **AI Scoring**: Machine learning model scores resumes on a 0-10 scale
- **Skill Extraction**: Automatically identifies technical skills from resume content
- **Experience Analysis**: Extracts years of experience information
- **Templates**: Pre-built resume templates for testing
- **Statistics Dashboard**: Track analysis metrics and trends
- **History Tracking**: View past analysis results
- **Modern UI**: Responsive web interface with professional design

## Technology Stack

- **Backend**: Python Flask API
- **Frontend**: Vanilla JavaScript with modern CSS
- **Machine Learning**: scikit-learn with TF-IDF vectorization
- **File Processing**: PyPDF2 for PDF parsing
- **Data Storage**: CSV dataset for model training

## Quick Start

1. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Train the Model**
   ```bash
   cd ml
   python train_model.py
   ```

3. **Start the Backend**
   ```bash
   cd backend
   python app.py
   ```

4. **Open Frontend**
   - Open `frontend/index.html` in your browser
   - Or serve it through a local web server

## API Endpoints

- `POST /api/rank-resume` - Analyze a resume file
- `GET /api/statistics` - Get analysis statistics
- `GET /api/history` - Get analysis history
- `GET /api/templates` - Get resume templates

## Project Structure

```
smart-resume-ranker/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── requirements.txt       # Python dependencies
│   ├── model/
│   │   └── ranker.py         # ML ranking logic
│   └── utils/
│       └── parser.py         # Resume parsing utilities
├── ml/
│   ├── train_model.py        # Model training script
│   └── resume_dataset.csv    # Training data
├── frontend/
│   └── index.html            # Web interface
├── test_resume1.txt          # Sample resume 1
├── test_resume2.txt          # Sample resume 2
└── README.md                 # This file
```

## Usage

1. Upload a resume file (PDF or TXT) or paste resume text
2. Click "Analyze Resume" to get AI-powered scoring
3. View detailed results including score, rank, skills found, and experience
4. Explore templates, statistics, and analysis history in other tabs

## Development

The system uses a linear regression model trained on resume data to predict resume quality scores. The model considers factors like skills mentioned, experience level, and overall content quality.

## License

MIT License - feel free to use and modify for your projects.
