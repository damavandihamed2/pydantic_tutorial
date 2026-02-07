from pydantic import BaseModel


class Circle(BaseModel):
    center_x: int = 0
    center_y: int = 0
    radius: int = 1
    name: str | None = None

c1 = Circle(radius=2)
Circle.model_fields.keys() - c1.model_fields_set



class Model(BaseModel):
    field_1: int = 1
    field_2: int | None = None
    field_3: str
    field_4: str | None = "Python"

m1 = Model(field_3="m1")
m2 = Model(field_1=1, field_2=None, field_3="m2", field_4="Python")
m3 = Model(field_1=1, field_2=None, field_3="m2", field_4="Python")


m1.model_dump()
m1.model_fields_set
m1.model_dump(include=m1.model_fields_set)

m2.model_dump(include=m2.model_fields_set)
print(m2.model_dump_json(indent=4))
