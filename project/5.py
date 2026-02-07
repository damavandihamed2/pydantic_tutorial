from uuid import uuid4
from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_serializer, UUID4
from pydantic.alias_generators import to_camel


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
    manufacturer: str
    series_name: str
    type_: AutomobileType = Field(alias="type")
    is_electric: bool = False
    manufactured_date: date = Field(alias="completionDate", ge=date(1980, 1, 1))
    base_msrp_usd: float = Field(validation_alias="msrpUSD", serialization_alias="baseMSRPUSD")
    vin: str
    number_of_doors: int = Field(default=4, validation_alias="doors", ge=2, le=4, multiple_of=2)
    registration_country: str | None = None
    license_plate: str | None = None

    @field_serializer("manufactured_date", when_used="json")
    def manufacture_date(self, value):
        return value.strftime("%Y/%m/%d")


a1 = Automobile(manufacturer="Sedan", series_name="1", type_=AutomobileType.sedan)

