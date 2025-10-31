# Frontend Documentation

## Overview
The frontend provides a modern, responsive web interface for the Smart Resume Ranker application. Built with vanilla HTML, CSS, and JavaScript for simplicity and fast loading.

## Features
- Drag & drop file upload
- Real-time resume analysis results
- Interactive score visualization
- Skills display with tags
- Ranking history view
- Statistics dashboard
- Responsive design for mobile and desktop

## File Structure
- `index.html` - Main application interface
- `resume_templates.json` - Predefined resume templates

## Browser Compatibility
- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 79+

## API Integration
The frontend communicates with the backend API at `http://localhost:5000/api` for:
- Resume ranking (`POST /api/rank-resume`)
- History retrieval (`GET /api/history`)
- Statistics (`GET /api/statistics`)
- Templates (`GET /api/templates`)

## Usage
1. Open `index.html` in a modern web browser
2. Upload a resume file using drag & drop or file picker
3. View analysis results including score, rank, and skills
4. Check statistics and history in the dashboard

## Styling
- Modern gradient backgrounds
- Card-based layout
- Smooth animations and transitions
- Mobile-responsive grid system
- Accessible color schemes
