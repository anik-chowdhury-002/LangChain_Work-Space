from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableBranch, RunnablePassthrough


load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a Detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize the following text \n {text}',
    input_variables=['text']
)


model1 = ChatGroq(
    model='openai/gpt-oss-20b'
)


parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model1, parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model1, parser)),
    RunnablePassthrough()
)

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke({'topic': 'AI Development history'})

print(result)

final_chain.get_graph().print_ascii()