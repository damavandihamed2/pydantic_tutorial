from pydantic import BaseModel, ValidationError, ConfigDict, Field

class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(validation_alias="FirstName",
                            alias="FirstName",
                            serialization_alias="givenName")



m = Model(FirstName="John")
m.model_dump(by_alias=True)





