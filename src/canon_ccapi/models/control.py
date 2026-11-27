from pydantic import BaseModel
from typing import Literal

class ShutterButton(BaseModel):
    af: bool # AF enable/disable

class ShutterButtonManual(BaseModel):
    action: Literal["release", "half_press", "full_press"]
    af: bool # AF enable/disable

class IgnoreShootingModeDial(BaseModel):
    status: Literal["on", "off"]

class MovieMode(BaseModel):
    status: Literal["on", "off"] #Move mode status

class RecordButton(BaseModel):
    action: Literal["start", "stop"] #Movie recording status

#class ZoomAbility(BaseModel):
#    min: int #Minimum zoom value
#    max: int #Maximum zoom value
#    step: int #Zoom step value


class DriveFocus(BaseModel):
    value: Literal["near1", "near2", "near3", "far1", "far2", "far3"]

class Autofocus(BaseModel):
    action: Literal["start", "stop"] #Autofocus action

class FlickerDetection(BaseModel):
    action: str #Flicker detection status

class HFFlickerDetection(BaseModel):
    action: str #High-frequency flicker detection status
    apply_result: bool #Whether to apply the set the camera to the recommended Tv value obtained from the detection results

class HFFlickerDetectionTV(BaseModel):
    value: Literal["decrement_large", "decrement_small", "increment_large", "increment_small"] #High-frequency flicker detection recommended Tv value
