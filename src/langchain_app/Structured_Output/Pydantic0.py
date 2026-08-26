from pydantic import BaseModel

class Person(BaseModel):

    name: str
    age: int

person_1: Person = {
    'name' : 'Anik',
    'age' : 22
}

person = Person(**person_1)

print(person)
print(type(person))