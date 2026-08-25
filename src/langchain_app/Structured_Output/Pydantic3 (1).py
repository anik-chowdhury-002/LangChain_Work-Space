from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):

    name: str
    age: Optional[int]

person_1: Person = {
    'name' : 'Anik',
    'age' : '32'
}

person = Person(**person_1)

print(person)
