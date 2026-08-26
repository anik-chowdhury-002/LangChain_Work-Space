#with structed output 

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = ('gemini-3.6-flash')
    
)

class Review(TypedDict):

    summary : str
    keywords : str
    sentiment : str

struct_model = model.with_structured_output(Review)

result = struct_model.invoke('''Really smooth and comfortable to use for everyday work.
The clicks are quiet, and the battery lasts surprisingly long.
It feels lightweight but still has a decent build quality.
The only downside is that the scroll wheel could be a little smoother.
Overall, a solid budget-friendly mouse that I’d recommend.''')

print(result)