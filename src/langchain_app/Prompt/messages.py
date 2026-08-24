from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

message_history = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain"),
]

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
    )

result = model.invoke(message_history)

message_history.append(AIMessage(content=result.content)) 

print(message_history)