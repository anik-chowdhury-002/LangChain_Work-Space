from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash" 
)

template = load_prompt('template.json')

chain = template | model | StrOutputParser()

st.header("Research Assistant")

paper_input = st.selectbox(
    "Select Research Paper Name", 
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
) 

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)


# বাটনে ক্লিক করলেই শুধুমাত্র একবার চেইন কল হবে
if st.button("Submit"):
    with st.spinner("Generating summary..."):
        result = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })
        st.write(result)