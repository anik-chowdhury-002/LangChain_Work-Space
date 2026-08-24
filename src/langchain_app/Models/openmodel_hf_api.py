#Through Hugging Face API key

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V4-Pro-0813",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the Capital of India")
print(response.content )

