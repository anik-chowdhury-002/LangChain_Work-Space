from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Person(BaseModel):

    name: str
    age: Optional[int] = Field(default=None)
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, description='A decimal value represent the grade of a student')
    

person_1: Person = {
    'name' : 'Anik',
    'email' : 'abc@abc.com',
    'cgpa' : '9' 
}

person = Person(**person_1)

person_dict = dict(person)


print(person)
print(person_dict)
