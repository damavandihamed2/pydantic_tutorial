from typing import Annotated, TypeVar
from uuid import uuid4
from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_serializer, UUID4
from pydantic.alias_generators import to_camel


T = TypeVar('T')
BoundedString = Annotated[str, Field(min_length=2, max_length=50)]
BoundedList = Annotated[list[T], Field(min_length=1, max_length=5)]

class AutomobileType(Enum):
    sedan = "Sedan"
    coupe = "Coupe"
    convertible = "Convertible"
    suv = "SUV"
    truck = "Truck"


class Automobile(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
        validate_default=True,
        validate_assignment=True,
        alias_generator=to_camel,
    )
    id_: UUID4 = Field(alias="id", default=uuid4)
    manufacturer: BoundedString
    series_name: BoundedString
    type_: AutomobileType = Field(alias="type")
    is_electric: bool = False
    manufactured_date: date = Field(alias="completionDate", ge=date(1980, 1, 1))
    base_msrp_usd: float = Field(validation_alias="msrpUSD", serialization_alias="baseMSRPUSD")
    top_features: BoundedList[BoundedString] | None = None
    vin: BoundedString
    number_of_doors: int = Field(default=4, validation_alias="doors", ge=2, le=4, multiple_of=2)
    registration_country: BoundedString | None = None
    license_plate: BoundedString | None = None


    @field_serializer("manufactured_date", when_used="json")
    def manufacture_date(self, value):
        return value.strftime("%Y/%m/%d")


a1 = Automobile(manufacturer="Sedan", series_name="1", type_=AutomobileType.sedan)

