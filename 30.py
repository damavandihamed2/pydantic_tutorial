from pydantic import BaseModel, ValidationError, ConfigDict, Field
from pydantic.alias_generators import to_camel

class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id_: int = Field(alias="id")
    first_name: str = Field(alias="firstName")



try:
    Model(id_=10, first_name="Newton")
except ValidationError as e:
    print(e)

Model.model_validate({"id_": 10, "first_name": "Newton"})




class Person(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
        extra="forbid",
    )
    id_: int = Field(alias="id", default=1)
    first_name: str | None = None
    last_name: str
    age: int | None = None


p = Person(id_=10, first_name="Isaac", lastName="Newton")

