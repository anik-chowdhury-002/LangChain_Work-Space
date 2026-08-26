
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt = PromptTemplate(
    template='genarate 5 interesting facts about {topic} in {Language}',
    input_variables=['topic', 'Language']

)


model = ChatGroq(
    model="allam-2-7b",
    temperature=0,
    )

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Cricket' , 'Language':'English'})

print(result)

chain.get_graph().print_ascii()