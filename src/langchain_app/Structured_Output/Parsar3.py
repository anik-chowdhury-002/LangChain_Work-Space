#JSON Output Parsar ... Structure decided by LLM, that is flaw...we doesnot enforce the schema

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

parsar = JsonOutputParser()

templete = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parsar.get_format_instructions()}
)

chain = templete | model | parsar
result = chain.invoke({'topic': 'GenAI'})


print(result)
print(type(result))





