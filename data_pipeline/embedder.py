# File: data_pipeline/embedder.py
from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("processed_jobs.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

vectors = []
for doc in docs:
    embedding = client.embeddings.create(
        input=doc["text"],
        model="text-embedding-3-small"
    ).data[0].embedding
    vectors.append({
        "id": doc["id"],
        "text": doc["text"],
        "embedding": embedding
    })

with open("vectors.json", "w", encoding="utf-8") as f:
    json.dump(vectors, f)
