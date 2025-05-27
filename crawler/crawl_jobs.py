# File: crawler/crawl_jobs.py
import json

mock_data = [
    {
        "title": "AI Engineer",
        "company": "OpenAI",
        "location": "Remote",
        "skills": ["Python", "LLM", "ML"],
        "salary": "4000-6000 USD",
        "description": "Build AI agents using LLMs and vector DBs."
    },
    {
        "title": "Backend Developer",
        "company": "TechCorp",
        "location": "Hà Nội",
        "skills": ["Django", "PostgreSQL"],
        "salary": "1000-1500 USD",
        "description": "Phát triển backend cho hệ thống nội bộ."
    }
]

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(mock_data, f, ensure_ascii=False, indent=2)
