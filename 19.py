from pydantic import BaseModel, ValidationError, ConfigDict

class Model(BaseModel):
    model_config = ConfigDict(validate_default=True)

    field_1: int = None
    field_2: str = 100

m = Model()


