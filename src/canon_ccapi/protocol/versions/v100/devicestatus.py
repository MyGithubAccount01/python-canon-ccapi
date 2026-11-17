from typing import Literal
from pydantic import BaseModel

class StorageListV100(BaseModel):
    name: str
    url: str
    accesscapability: Literal["readonly", "readwrite"]
    maxsize: int
    spacesize: int
    contentsnumber: int

class StorageV100(BaseModel):
    storagelist: list[StorageListV100]