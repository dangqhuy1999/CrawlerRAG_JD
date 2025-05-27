# File: data_pipeline/preprocess.py
import json

with open("jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

docs = []
for job in jobs:
    content = f"{job['title']} tại {job['company']} - {job['location']}. Kỹ năng: {', '.join(job['skills'])}. Lương: {job['salary']}. Mô tả: {job['description']}"
    docs.append({"id": job["title"], "text": content})

with open("processed_jobs.json", "w", encoding="utf-8") as f:
    json.dump(docs, f, ensure_ascii=False, indent=2)
