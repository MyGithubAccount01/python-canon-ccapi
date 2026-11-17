from typing import Literal
from pydantic import BaseModel


class StorageListV110(BaseModel):
    name: str
    path: str
    accesscapability: Literal["readonly", "readwrite"]
    maxsize: int
    spacesize: int
    contentsnumber: int


class StorageV110(BaseModel):
    storagelist: list[StorageListV110]