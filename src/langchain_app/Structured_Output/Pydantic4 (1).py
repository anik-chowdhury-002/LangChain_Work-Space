from pydantic import BaseModel, EmailStr
from typing import Optional

class Person(BaseModel):

    name: str
    age: Optional[int]
    email : EmailStr
    

person_1: Person = {
    'name' : 'Anik',
    'age' : '32',
    'email' : 'abc@abc.com' 
}

person = Person(**person_1)

print(person)
