import re
from PyPDF2 import PdfReader

class ResumeParser:
    def __init__(self):
        pass

    def parse_text_file(self, file_path):
        """Parse text resume file"""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def parse_pdf_file(self, file_path):
        """Parse PDF resume file"""
        reader = PdfReader(file_path)
        content = ""
        for page in reader.pages:
            content += page.extract_text()
        return content

    def extract_skills(self, text):
        """Extract skills from resume text"""
        # Common skills keywords
        skills_keywords = [
            'python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust',
            'html', 'css', 'react', 'angular', 'vue', 'node.js', 'django', 'flask',
            'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'aws', 'azure', 'gcp',
            'docker', 'kubernetes', 'git', 'linux', 'tensorflow', 'pytorch', 'scikit-learn',
            'machine learning', 'data science', 'artificial intelligence', 'deep learning'
        ]

        text_lower = text.lower()
        found_skills = [skill for skill in skills_keywords if skill in text_lower]

        return found_skills

    def extract_experience_years(self, text):
        """Extract years of experience from resume text"""
        # Pattern to find years of experience
        patterns = [
            r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
            r'experience\s*(?:of\s*)?(\d+)\+?\s*years?',
            r'(\d+)\+?\s*years?\s*(?:of\s*)?(?:work|professional)\s*experience'
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return int(match.group(1))

        # Default to 0 if no experience found
        return 0
