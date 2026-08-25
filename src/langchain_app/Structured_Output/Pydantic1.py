from pydantic import BaseModel

class Person(BaseModel):

    name: str = 'Anik'
    age: int =  22

person_1: Person = {}

person = Person(**person_1)

print(person)