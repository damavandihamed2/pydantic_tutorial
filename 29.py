from pprint import pprint
from pydantic import BaseModel, Field, ValidationError, ConfigDict
from pydantic.alias_generators import to_camel, to_snake, to_pascal

def make_upper(in_str: str) -> str:
    return in_str.upper()



class Person(BaseModel):
    model_config = ConfigDict(alias_generator=make_upper)
    id_: int
    first_name: str | None = None
    last_name: str
    age: int | None = None

pprint(Person.model_fields)
p = Person(ID_=1, LAST_NAME="Fourier", AGE=62)
p.model_dump()
p.model_dump(by_alias=True)




class Person(BaseModel):
    model_config = ConfigDict(alias_generator=make_upper)
    id_: int = Field(alias="ID")
    first_name: str | None = None
    last_name: str
    age: int | None = None

pprint(Person.model_fields)
p = Person(ID=1, LAST_NAME="Fourier", AGE=62)
p.model_dump()
p.model_dump(by_alias=True)




