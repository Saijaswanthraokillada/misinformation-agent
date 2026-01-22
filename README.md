# Convolve 4.0 – Misinformation Detection Agent
Overview
This project is a Misinformation Detection Agent built for Convolve 4.0 Round 2.  
It uses Qdrant as a vector database and SentenceTransformer embeddings (1536D) to detect and retrieve semantically similar misinformation claims.  
Supports both text input and image input (OCR).

---

## Setup Instructions

1. Clone the Repository
'''bash
git clone https://github.com/Saijaswanthraokillada/misinformation-agent
cd misinformation-agent
2.install dependencies
pip install -r requirements.txt
3. Configure API Keys
-Replace YOUR-QDRANT-API-KEY in qdrant_utils.py with your Qdrant Cloud API key.
- Replace YOUR-CLUSTER-ENDPOINT with your Qdrant Cloud endpoint.
USAGE:
RUN the demo:
'''bash
python main.py
COMMANDS:
-INSERT A TEXT: insert COVID vaccine causes infertility
saearch by text: search vaccines affect infertility
search by image: search_img sampleimage.jpg
EXIT:
exit

