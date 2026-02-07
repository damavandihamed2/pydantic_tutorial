from typing import Any
from dateutil.parser import parse
from datetime import datetime
from pydantic import BaseModel, field_validator, ValidationError


class Model(BaseModel):
    dt: datetime

try:
    Model(dt="2020/1/1 3:00pm")
except ValidationError as e:
    print(e)

try:
    Model(dt="Jan 1, 2020 3:00pm")
except ValidationError as e:
    print(e)


parse("2020/1/1 3:00pm")
parse("Jan 1, 2020 3:00pm")



class Model(BaseModel):
    dt: datetime
    @field_validator("dt", mode="before")
    @classmethod
    def parse_datetime(cls, value: Any):
        if isinstance(value, str):
            print("Parsing String")
            try:
                return parse(value)
            except Exception as e:
                raise ValueError(str(e))
        print("Pass through...")
        return value


Model(dt="2020/1/1 3:00pm")
Model(dt=datetime(2020, 1, 1))



