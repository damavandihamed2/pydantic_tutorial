from pydantic import BaseModel, ConfigDict, Field


response_json = """
{
    "ID": 100,
    "FirstName": "Isaac",
    "lastname": "Newton"
}
"""

class Person(BaseModel):

    model_config = ConfigDict()

    id_: int = Field(alias="ID", serialization_alias="id")
    first_name: str = Field(alias="FirstName", serialization_alias="firstName")
    last_name: str = Field(alias="lastname", serialization_alias="lastName")

p = Person.model_validate_json(response_json)

p.model_dump(by_alias=True)




