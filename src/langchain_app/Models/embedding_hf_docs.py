from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",

)

texts = "I am a very good person"


embeddings = embedding.embed_query(texts)
print(str(embeddings))