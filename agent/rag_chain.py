# File: agent/rag_chain.py
from qdrant_client import QdrantClient
from openai import OpenAI
import os

client_qdrant = QdrantClient("localhost", port=6333)
client_llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_jobs(query: str) -> str:
    embedded = client_llm.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    ).data[0].embedding

    hits = client_qdrant.search(
        collection_name="jobs",
        query_vector=embedded,
        limit=3
    )
    context = "\n---\n".join(hit.payload["text"] for hit in hits)

    prompt = f"""
### Context:
{context}

### Question:
{query}

### Answer:
"""
    completion = client_llm.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return completion.choices[0].message.content.strip()
