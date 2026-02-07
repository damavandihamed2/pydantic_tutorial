from datetime import datetime
import pytz

from pydantic import BaseModel, field_serializer, FieldSerializationInfo


class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer("dt", when_used="always")
    def serialize_name(self, value):
        print(f"type={type(value)}")
        return value

m = Model(dt="2020-01-01T12:00:00")
m.model_dump_json()




class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer("dt", when_used="json-unless-none")
    def serialize_name(self, value):
        print(f"type={type(value)}")
        return value.strftime("%Y/%-m/%-d %I:%M %p")

m = Model(dt="2020-01-01T12:00:00")
m.model_dump()
m.model_dump_json()









class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer("dt", when_used="unless-none")
    def serialize_name(self, value, info: FieldSerializationInfo):
        print(f"info={info}")
        print(f"is_json={info.mode_is_json()}")
        return value


m = Model(dt=datetime(2020, 1, 1))
m.model_dump()
m.model_dump_json()





def make_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt

dt = make_utc(datetime.now())
dt.isoformat()
dt = make_utc(datetime.now())


def dt_utc_json_serializer(dt: datetime) -> str:
    dt = make_utc(dt)
    return dt.strftime("%Y-%-m-%-dT%H:%M:%SZ")


class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer("dt", when_used="unless-none")
    def serialize_name(self, value, info: FieldSerializationInfo):
        if info.mode_is_json():
            return dt_utc_json_serializer(value)
        return make_utc(value)



m = Model(dt=datetime(2020, 1, 1))
m.model_dump()
m.model_dump_json()


eastern = pytz.timezone("US/Eastern")
dt = eastern.localize(datetime(2020, 1, 1))
dt.isoformat()
m = Model(dt=dt)
m
m.model_dump()
m.model_dump_json()
