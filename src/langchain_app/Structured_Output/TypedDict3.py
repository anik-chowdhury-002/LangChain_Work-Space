#with structed output with anotation 

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = ('gemini-3.6-flash')
    
)

class Review(TypedDict):

    summary : Annotated[str, "A Brief Summary of the review" ]
    keywords : Annotated[str, "A Keywords from the review" ]
    sentiment : Annotated[Literal["+Ve", "-Ve", "Mixed"], "return sentiment from the review" ]
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review " ]
    pros: Annotated[Optional[list[str]], "Write down all Pros inside a list "]
    cons: Annotated[Optional[list[str]], "Write down all Cons inside a list "]
    name: Annotated[Optional[str], "Write the Name of the Reviewer (the person only)" ]

struct_model = model.with_structured_output(Review)

result = struct_model.invoke('''The mouse feels comfortable and responsive, with a smooth tracking experience and solid build quality.
Battery life is impressive, and the lightweight design makes it convenient for everyday work.
However, the scroll wheel could be smoother, and the buttons may feel slightly stiff at times.
The lack of advanced customization is also a drawback for power users.
Overall, it’s a good value-for-money option for regular use, but not ideal for demanding users.

reviewed by Anik Chowdhury

''')

print(result)