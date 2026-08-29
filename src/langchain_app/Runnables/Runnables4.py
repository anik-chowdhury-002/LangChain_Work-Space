from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda


load_dotenv()

#make the word counder to a runnable using RunnableLambda
def word_counter(text):
    return len(text.split())

prompt = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatGroq(
    model='openai/gpt-oss-20b'
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})

final_chain = joke_gen_chain | parallel_chain



result = final_chain.invoke({"topic":"Cricket"})

print(result)



