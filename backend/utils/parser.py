import re
import os

class ResumeParser:
    def __init__(self):
        pass

    def parse_text_file(self, file_path):
        """Parse resume from text file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def parse_pdf_file(self, file_path):
        """Parse resume from PDF file (placeholder for future implementation)"""
        # For now, return a message indicating PDF parsing is not implemented
        return "PDF parsing not implemented yet. Please use text files."

    def extract_skills(self, text):
        """Extract skills from resume text"""
        skills_keywords = [
            'python', 'java', 'javascript', 'html', 'css', 'react', 'node.js',
            'sql', 'mysql', 'postgresql', 'mongodb', 'aws', 'docker', 'kubernetes',
            'machine learning', 'data science', 'tensorflow', 'pytorch', 'pandas',
            'numpy', 'scikit-learn', 'git', 'agile', 'scrum'
        ]

        found_skills = []
        text_lower = text.lower()

        for skill in skills_keywords:
            if skill in text_lower:
                found_skills.append(skill.title())

        return found_skills

    def extract_experience_years(self, text):
        """Extract years of experience from resume text"""
        # Look for patterns like "5 years", "3+ years", etc.
        patterns = [
            r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
            r'experience\s*(?:of\s*)?(\d+)\+?\s*years?',
            r'(\d+)\+?\s*years?\s*(?:of\s*)?work'
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return int(match.group(1))

        return 0  # Default if no experience found
