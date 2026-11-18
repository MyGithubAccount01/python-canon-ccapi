from pydantic import BaseModel, Field, model_validator
from typing import Literal

AccessCapability = Literal["readonly", "readwrite"]
BatteryKind = Literal["battery", "not_inserted", "ac_adapter", "dc_coupler", "unknown", "batterygrip"]
BatteryLevel = Literal["low", "quarter", "half", "high", "full", "unknown", "charge", "chargestop", "chargecomp", "none"]
BatteryQuality = Literal["bad", "normal", "good","unknown"]

class StorageList(BaseModel):
    # Fields based on actual CCAPI response
    name: str # Name of the storage cfex, sd
    url: str | None = None # URL of the storage location
    path: str | None = None # URL of the storage location
    access_capability: AccessCapability = Field(validation_alias="accesscapability") # Access capability of the storage (readwrite/readonly)
    max_size: int = Field(validation_alias="maxsize") # Maximum size of the storage
    space_size: int = Field(validation_alias="spacesize") # Available space in the storage
    contents_number: int = Field(validation_alias="contentsnumber") # Number of items in the storage

    @model_validator(mode="after")
    def validate_location(self):
        if (self.url is None) == (self.path is None):
            raise ValueError("Either url or path must be provided, but not both.")
        return self

class Storage(BaseModel):
    storageList: list[StorageList] = Field(validation_alias="storagelist")

class CurrentStorage(BaseModel):
    # Fields based on actual CCAPI response
    name: str # Name of the current storage. If empty media is not inserted.
    path: str # Path of the current storage. If empty media is not inserted.

class CurrentDirectory(BaseModel):
    # Fields based on actual CCAPI response
    name: str # Name of the current directory. If empty, no directory is selected.
    path: str # Path of the current directory. If empty, no directory is selected.

class Battery(BaseModel):
    # Fields based on actual CCAPI response
    name: str # Name of the battery. If empty, no battery is inserted.
    kind: str # Kind of the battery. If empty, no battery is inserted.
    level: str # Battery level. If empty, no battery is inserted.
    quality: str # Quality of the battery. If empty, no battery is inserted.

class BatteryList(BaseModel):
    # Fields based on actual CCAPI response
    pass

class Lens(BaseModel):
    # Fields based on actual CCAPI response
    pass

class Temperature(BaseModel):
    # Fields based on actual CCAPI response
    pass

class PowerZoomStatus(BaseModel):
    # Fields based on actual CCAPI response
    pass