from typing import Union, Optional
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    field: int
try: Model(field=None)
except ValidationError as e: print(e)


class Model(BaseModel):
    field: int | None
try: Model(field=None)
except ValidationError as e: print(e)


class Model(BaseModel):
    field: int | None = None
try: Model()
except ValidationError as e: print(e)


class Model(BaseModel):
    field_1: int | None
    field_2: Union[int, None]
    field_3: Optional[int]


class Model(BaseModel):
    field: int = None
try: Model(field=None)
except ValidationError as e: print(e)






