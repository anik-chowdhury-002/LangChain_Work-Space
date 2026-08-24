from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    dimensions=32
    #google_api_key=os.getenv("GOOGLE_API_KEY")
)

documents = [
    "I am a very good person",
    "I am a very bad person",
    "I am a neutral person",
    "I am a fan of cricket"
]

result = embedding.embed_documents(documents)
print(str(result))
