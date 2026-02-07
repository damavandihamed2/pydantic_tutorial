from pydantic import BaseModel

class Circle(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: int


data = {"radius": 1}
data_json = '{"radius": 1}'

Circle.model_validate(data)
Circle.model_validate_json(data_json)
