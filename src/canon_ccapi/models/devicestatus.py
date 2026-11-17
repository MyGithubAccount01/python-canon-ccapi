from pydantic import BaseModel
from typing import Literal

AccessCapability = Literal["readonly", "readwrite"]

class StorageList(BaseModel):
    # Fields based on actual CCAPI response
    name: str # Name of the storage cfex, sd
    contents_path: str # URL of the storage location
    access_capability: AccessCapability # Access capability of the storage (readwrite/readonly)
    max_size: int # Maximum size of the storage
    space_size: int # Available space in the storage
    contents_number: int # Number of items in the storage

class Storage(BaseModel):
    storageList: list[StorageList]

class CurrentStorage(BaseModel):
    # Fields based on actual CCAPI response
    pass

class CurrentDirectory(BaseModel):
    # Fields based on actual CCAPI response
    pass

class Battery(BaseModel):
    # Fields based on actual CCAPI response
    pass

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