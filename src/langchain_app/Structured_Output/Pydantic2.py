from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):

    name: str
    age: Optional[int]

person_1: Person = {
    'name' : 'Anik',
    'age' : None
}

person = Person(**person_1)

print(person)
