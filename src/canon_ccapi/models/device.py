from pydantic import BaseModel, Field, ConfigDict

class DeviceInformation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    manufacturer: str = Field(alias="munufacturer")
    productname: str
    guid: str
    serialnumber: str
    macaddress: str
    firmwareversion: str