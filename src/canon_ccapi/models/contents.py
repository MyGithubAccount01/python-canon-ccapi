from pydantic import BaseModel
from typing import Literal

ContentType = Literal["all", 
                      "jpeg", 
                      "cr2", 
                      "cr3", 
                      "wav",
                      "mp4",
                      "mov"
]
ContentKind = Literal["list",
                      "chunked"
]

ContentOrder = Literal["asc", 
                       "desc"
]

GetContentsKind = Literal["main",
                          "thumbnail",
                          "display",
                          "embedded",
                          "info"
]

ModifyContentsAction = Literal["rotate",
                               "protect",
                               "archive",
                               "rating"
]

ModifyContentsValue = Literal["0", "90", "180", "270",
                               "enable", "disable",
                               "off", "1", "2", "3", "4", "5"
]

ContentsModification = (
    RotateContents
    | ProtectContents
    | ArchiveContents
    | RateContents
    | GPSContents
    | XMPDescriptionContents
)

class Contents(BaseModel):
    url: list[str] #Storage URLs

class Storage(BaseModel):
    url: list[str] #Directory URLs

class ContentURL(BaseModel):
    url: list[str] #Content URL

class DeleteDirectory(BaseModel):
    storage: str #Storage URL
    directory: str #Directory URL

class GetContents(BaseModel):
    storage: str #Storage URL
    directory: str #Directory URL
    file: str #File name
    kind: GetContentsKind | None = None #Content kind

class ModifyContents(BaseModel):
    action: ModifyContentsAction #Action to perform on the content
    value: ModifyContentsValue #Directory URL

class GPSTime(BaseModel):
    hour: RationalPair
    minute: RationalPair
    second: RationalPair

class GPS(BaseModel):
    latitude_ref: Literal["N", "S"]
    latitude: GPSCoordinate

    longitude_ref: Literal["E", "W"]
    longitude: GPSCoordinate

    altitude_ref: Literal["P", "M"]
    altitude: RationalPair

    timestamp: GPSTime
    mapdatum: str
    status: Literal["A", "V"]
    datestamp: str

class GPSContents(BaseModel):
    action: Literal["gps"]
    gps: GPS

class XMPDescriptionContents(BaseModel):
    action: Literal["xmp_description"]
    value: str

class RotateContents(BaseModel):
    action: Literal["rotate"]
    value: Literal["0", "90", "180", "270"]

class ProtectContents(BaseModel):
    action: Literal["protect"]
    value: Literal["enable", "disable"]

class ArchiveContents(BaseModel):
    action: Literal["archive"]
    value: Literal["enable", "disable"]

class RateContents(BaseModel):
    action: Literal["rating"]
    value: Literal["off", "1", "2", "3", "4", "5"]