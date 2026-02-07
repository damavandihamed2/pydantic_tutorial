from pydantic import BaseModel
from pprint import pprint


class Model(BaseModel):
    field_1: int | None = None
    field_2: str = "Python"

Model.model_json_schema()

pprint(Model.model_json_schema())
