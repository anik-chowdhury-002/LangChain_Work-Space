#JSON Output Parsar

#String Output Parsar
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

chat = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    task="text-generation"
)

model = ChatHuggingFace(llm = chat)

parsar = JsonOutputParser()

templete = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parsar.get_format_instructions()}
)

chain = templete | model | parsar
result = chain.invoke({})


print(result)
print(type(result))





