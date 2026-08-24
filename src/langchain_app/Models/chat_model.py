import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# টোকেন লিমিট সরিয়ে শুধু মডেল কল করা হয়েছে
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# StrOutputParser যেকোনো মেটাডেটা বা লিস্ট ছেঁকে শুধু মূল টেক্সট বের করে আনবে
chain = model | StrOutputParser()

response = chain.invoke("Write a poem on indian cricket")
print(response)