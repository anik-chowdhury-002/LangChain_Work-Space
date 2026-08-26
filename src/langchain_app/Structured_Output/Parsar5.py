#PydanticOutputParser - for data Validation

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()


model = ChatGroq(
    model="allam-2-7b",
    temperature=0,
    )

class Person (BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the person')

    

parser = PydanticOutputParser(pydantic_object=Person)

templete = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = templete.invoke({'place':'Srilanka'})
#print(prompt)

chain = templete | model | parser

result = chain.invoke(prompt)

print(result)