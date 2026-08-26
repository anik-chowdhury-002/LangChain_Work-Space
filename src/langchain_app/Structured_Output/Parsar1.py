#Without Parsar
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

templete1 = PromptTemplate(
    template='write detailed report on {topic}',
    input_variables=['topic']
)

templete2 = PromptTemplate(
    template='write 5 line summary on the following text. \n{text}',
    input_variables=['text']
)


prompt1 = templete1.invoke({'topic':'black hole'})

result_1 = model.invoke(prompt1)

prompt2 = templete2.invoke({'text': result_1.content})

result_2 = model.invoke(prompt2)

print(result_2.content)