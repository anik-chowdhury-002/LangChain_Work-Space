#structed output with Pydantic

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = ('gemini-3.6-flash')
    
)

class Review(BaseModel):

    key_themes : list[str] = Field(description="Write down all the key themes discussed in the review ")
    summary : str = Field(description="A Brief Summary of the review")
    sentiment : Literal["+Ve", "-Ve", "Mixed"] = Field(description="return sentiment from the review")
    pros: Optional[list[str]] = Field(default=None , description="Write down all Pros inside a list " )
    cons: Optional[list[str]] = Field(default=None , description="Write down all cons inside a list " )
    name: Optional[str] = Field(default=None, description="Write the Name of the Reviewer (the person only)")


struct_model = model.with_structured_output(Review)

result = struct_model.invoke('''The mouse feels comfortable and responsive, with a smooth tracking experience and solid build quality.
Battery life is impressive, and the lightweight design makes it convenient for everyday work.
However, the scroll wheel could be smoother, and the buttons may feel slightly stiff at times.
The lack of advanced customization is also a drawback for power users.
Overall, it’s a good value-for-money option for regular use, but not ideal for demanding users.

reviewed by Anik Chowdhury

''')

print(result)