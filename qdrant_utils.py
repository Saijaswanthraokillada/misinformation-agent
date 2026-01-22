import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams
from embedding import generate_embedding

# Connect to Qdrant
client = QdrantClient(
    url="https://93a004ba-7fe6-41d8-82a1-995baf4a841a.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.QW_bRk6Hx1c-5tnte3dpmgUa99MC88SdRkGNGQ5B8m0",
)
# Ensure collection exists
client.create_collection(
    collection_name="misinforming",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    overwrite=True
)

def insert_claim(text: str, claim_id: int = None):
    """Insert a claim into Qdrant."""
    vector = generate_embedding(text)
    point = PointStruct(
        id=claim_id or hash(text),
        vector=vector,
        payload={"claim": text}
    )
    client.upsert(collection_name="misinforming", points=[point])
    print(f"Inserted claim: {text}")

def search_claim(text: str, top_k: int = 3):
    """Search for similar claims in Qdrant."""
    query_vector = generate_embedding(text)
    results = client.search(collection_name="misinforming", query_vector=query_vector, limit=top_k)
    print(f"\nSearch results for: {text}")
    for hit in results:
        print(f"Score: {hit.score:.4f}, Claim: {hit.payload['claim']}")