#StructuredOutputParser - here we can enforce shema but data validation not possible here.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema



load_dotenv()

chat = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    task="text-generation"
)

model = ChatHuggingFace(llm = chat)

schema = [
    ResponseSchema(name='fact_1', description = 'Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description = 'Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description = 'Fact 3 about the topic'),
    ResponseSchema(name='fact_4', description = 'Fact 4 about the topic'),
    ResponseSchema(name='fact_5', description = 'Fact 5 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

templete = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = templete | model | parser
result = chain.invoke({'topic': 'GenAI'})

print(result)