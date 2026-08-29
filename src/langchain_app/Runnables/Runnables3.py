from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel


load_dotenv()

prompt1 = PromptTemplate(
    template = 'Genarate a tweet about topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Genarate a linkedin post about topic {topic} in formal Language {Language}',
    input_variables=['topic','Language']
)


model1 = ChatGroq(
    model='openai/gpt-oss-20b'
)

model2 = ChatGroq(
    model='groq/compound'
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model1, parser),
    'linkedin': RunnableSequence(prompt2, model2, parser)
})

result = parallel_chain.invoke({'topic': 'AI', 'Language': 'English'})

print(result['tweet'])
print(result['linkedin'])

parallel_chain.get_graph().print_ascii()