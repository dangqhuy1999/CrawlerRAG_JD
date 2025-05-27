# File: data_pipeline/load_to_qdrant.py

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import json

client = QdrantClient("localhost", port=6333)

client.recreate_collection(
    collection_name="jobs",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

with open("vectors.json", "r", encoding="utf-8") as f:
    data = json.load(f)

points = [
    PointStruct(id=idx, vector=item["embedding"], payload={"text": item["text"]})
    for idx, item in enumerate(data)
]

client.upsert(collection_name="jobs", points=points)
