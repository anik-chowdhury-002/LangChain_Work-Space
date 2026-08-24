from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

chat_history = [
    SystemMessage(content="You are a helpful AI Medical Assistent, you have to give proper medical response")
]
chain = model | StrOutputParser()

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break

    result = chain.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("AI:", result)

print("Chat session ended.", chat_history)