from pydantic import BaseModel, ValidationError, ConfigDict

class Model(BaseModel):
    field: float

m = Model(field=1)
m.field = ""


class Model(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    field: float

m = Model(field=1)
try:
    m.field = ""
except ValidationError as e:
    print(e)
