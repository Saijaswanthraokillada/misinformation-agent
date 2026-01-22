import numpy as np
from sentence_transformers import SentenceTransformer

# Load a 768D model
model = SentenceTransformer("sentence-transformers/paraphrase-mpnet-base-v2")

def generate_embedding(text: str):
    """Generate a 1536D embedding by concatenating two 768D embeddings."""
    emb1 = model.encode(text)
    emb2 = model.encode(text[::-1])  # reversed text trick
    return np.concatenate([emb1, emb2]).tolist()