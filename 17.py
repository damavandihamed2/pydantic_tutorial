from pydantic import BaseModel, ConfigDict, ValidationError

class Model(BaseModel):

    model_config = ConfigDict(extra="forbid")

    field1: int


m = Model(field1=10, field_2=20)
m
dict(m)





