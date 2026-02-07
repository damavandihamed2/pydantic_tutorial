from pydantic import BaseModel, Field, field_validator, ValidationError

class Model(BaseModel):
    number: int = Field(gt=0, lt=10)
try:
    Model(number=12)
except ValidationError as e:
    print(e)


class Model(BaseModel):
    number: int = Field(gt=0, lt=10)
    @field_validator('number')
    @classmethod
    def validate_even(cls, value):
        print("running custom validator")
        print(f"{value=}, {type(value)=}")
        if value % 2 == 0:
            return value
        else:
            raise ValueError("value must be even")

try:
    Model(number=7)
except ValidationError as e:
    print(e)


class Model(BaseModel):
    number: int = Field(gt=0, lt=10)
    @field_validator('number')
    @classmethod
    def validate_even(cls, value):
        print("running custom validator")
        print(f"{value=}, {type(value)=}")
        if value % 2 == 0:
            return value
        raise TypeError("value must be even")

try:
    Model(number=7)
except Exception as e:
    print(e)



class Model(BaseModel):
    number: int = Field(gt=0, lt=10)
    @field_validator('number')
    @classmethod
    def validate_even(cls, value):
        print("running custom validator")
        print(f"{value=}, {type(value)=}")
        if value % 2 == 1:
            return value + 1
        return value

try:
    m = Model(number=7)
except Exception as e:
    print(e)








