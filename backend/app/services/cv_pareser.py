import random

def parse_cv_file(filename: str) -> dict:
    """Simulates CV parsing and skill extraction."""
    skills = random.sample(["Python", "SQL", "Docker", "React", "AWS"], k=3)
    return {"filename": filename, "skills": skills, "text": "..."}