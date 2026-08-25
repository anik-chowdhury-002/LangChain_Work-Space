from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

person_1: Person = {
    'name' : 'Anik',
    'age' : 22
}

print(person_1)