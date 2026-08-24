from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen3-0.6B",   
    task="text-generation",
    pipeline_kwargs={"max_new_tokens" : 512,"temperature" : 0.9}
)

model = ChatHuggingFace(
    llm =llm 
)

response = model.invoke("What is the Capital of India")
print(response.content)

