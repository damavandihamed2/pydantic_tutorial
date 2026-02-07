from pydantic import BaseModel, Field, ValidationError, ConfigDict


class Model(BaseModel):
    id_: int = Field(alias="id")
    last_name: str = Field(alias="lastName")

json_data = '''
{
    "id": 100,
    "lastName": "Gauss"
}
'''
m = Model.model_validate_json(json_data)

hasattr(m, "lastName")




class Model(BaseModel):
    id_: int = Field(alias="id", default=100)
    last_name: str = Field(alias="lastName")

m = Model(lastName="Gauss")



class Person(BaseModel):
    id_: int = Field(alias="id")
    first_name: str | None = Field(alias="firstName", default=None)
    last_name: str = Field(alias="lastName")
    age: int | None = None

isaac = Person(id=1, firstName="Isaac", lastName="Newton", age=84)

isaac.model_dump()
isaac.model_dump(by_alias=True)

isaac.model_dump_json()
isaac.model_dump_json(by_alias=True)

from pprint import pprint
pprint(Person.model_fields)







