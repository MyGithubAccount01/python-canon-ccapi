from pydantic import BaseModel, Field, model_validator
from typing import Literal

class Recordable(BaseModel):
    recordableshots: int #Number of recordable still images (This is null in movie mode.)
    remainingtime: int #Remaining recording time (seconds) (This is null in still image mode.)