
from pydantic import BaseModel

class AperatureValue(BaseModel):
    value: str #Level increment

class ShuterValue(BaseModel):
    value: str #Level increment

class ExposureValue(BaseModel):
    value: str #Level increment

class FlashValue(BaseModel):
    value: str #Level increment

class ISOValue(BaseModel):
    value: str #Level increment

