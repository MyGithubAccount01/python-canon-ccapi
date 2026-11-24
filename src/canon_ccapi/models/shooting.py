from pydantic import BaseModel, model_validator
from typing import Literal

#TODO: Implement
class Shooting(BaseModel):

class ShootingModeDial(BaseModel):
    value: Literal["m", 
                   "av", 
                   "tv", 
                   "p", 
                   "auto", 
                   "plus_movie_auto", 
                   "panoramic_shot", 
                   "sports", 
                   "fv", 
                   "a+", 
                   "scn",
                   "creativefilter",
                   "movie",
                   "c3",
                   "c2",
                   "c1",
                   "bulb"] #Shooting mode dial value

class ShootingModeDialMovie(BaseModel):
    value: Literal["auto", "video_blog", "manual", "hdr"] #Shooting mode dial movie value

class ShootingMode(BaseModel):
    value: Literal["m", 
                   "av", 
                   "tv", 
                   "p", 
                   "fv", 
                   "a+", 
                   "c3",
                   "c2",
                   "c1",
                   "bulb"] #Shooting mode value

class AV(BaseModel):
    value: str #Present value
    ability: list[str] #Ability values

class TV(BaseModel):
    value: str #Present value
    ability: list[str] #Ability values

class ISO(BaseModel):
    value: str #Present value
    ability: list[str] #Ability values

class Exposure(BaseModel):
    value: str #Present value
    ability: Literal[
        "-3.0", #Exposure compensation -3.0
        "-2_2/3", #Exposure compensation -2 2/3
        "-2_1/3", #Exposure compensation -2 1/3
        "-2.0", #Exposure compensation -2.0
        "-1_2/3", #Exposure compensation -1 2/3
        "-1_1/3", #Exposure compensation -1 1/3
        "-1.0", #Exposure compensation -1.0
        "-0_2/3", #Exposure compensation -0 2/3
        "-0_1/3", #Exposure compensation -0 1/3
        "+0.0", #Exposure compensation 0.0
        "+0_1/3", #Exposure compensation +0 1/3
        "+0_2/3", #Exposure compensation +0 2/3
        "+1.0", #Exposure compensation +1.0
        "+1_1/3", #Exposure compensation +1 1/3
        "+1_2/3", #Exposure compensation +1 2/3
        "+2.0", #Exposure compensation +2.0
        "+2_1/3", #Exposure compensation +2 1/3
        "+2_2/3", #Exposure compensation +2 2/3
        "+3.0" #Exposure compensation +3.0
    ] #Ability values

class WhiteBalance(BaseModel):
    value: str #Present value
    ability: Literal["auto", # Auto: Ambience priority
                     "awbwhite", # Auto: White priority
                     "daylight", # Sunlight
                     "shade", # Shade
                     "cloudy", # Cloudy
                     "tungsten", # Incandescent light bulb
                     "whitefluorescent", # White fluorescent light
                     "flash", # Flash
                     "custom", # Custom
                     "colortemp", # Color temp.
                     "colortemp2", # Color temp. 2
                     "colortemp3", # Color temp. 3
                     "colortemp4", # Color temp. 4
    ] #Ability values

class ColorTemperatureAbility(BaseModel):
    min: int
    max: int
    step: int

class ColorTemperature(BaseModel):
    value: str #Present value
    ability: ColorTemperatureAbility  #Ability values

class AFOperation(BaseModel):
    value: Literal["oneshot", "servo", "aifocus", "manual"] #Present value

class AFMethod(BaseModel):
    value: str #Present value
    ability: list[
        "face+tracking", #Face tracking priority AF
        "spot", #Single-point spot AF
        "1point", #Single-point AF
        "expand_cross", #Expanded area AF (up, down, left and right)
        "expand_around", #Expanded area AF (surrounding)
        "zone", #Zone AF
        "large_zone_vertical", #Large Zone AF: Vertical
        "large_zone_horizontal", #Large Zone AF: Horizontal
        "flexible_zone_1", #Flexible Zone AF 1
        "flexible_zone_2", #Flexible Zone AF 2
        "flexible_zone_3", #Flexible Zone AF 3
        "whole_area", #Whole area AF
        "notracking_spot", #No tracking Single-point spot AF
        "notracking_1point", #No tracking Single-point spot AF
        "notracking_expand_cross", #No tracking Expanded area AF (up, down, left and right)
        "notracking_expand_around", #No tracking Expanded area AF (surrounding)
    ] #Ability values

class TrackingSetting(BaseModel):
    value: str #Present value
    ability: Literal["enable", "disable"] #Ability values

#4.9.17
ShutterModeValue = Literal["elec_1st_curtain", "mechanical", "electronic"]
class ShutterMode(BaseModel):
    value: ShutterModeValue #Present value
    ability: list[ShutterModeValue] #Ability values

RawQuality = Literal["none", "raw", "craw"]

JpegQuality = Literal[
    "none",
    "large_fine",
    "large_normal",
    "medium_fine",
    "medium_normal",
    "small",
]

class StillImageQualityValue(BaseModel):
    raw: RawQuality
    jpeg: JpegQuality


class StillImageQualityAbility(BaseModel):
    raw: list[RawQuality]
    jpeg: list[JpegQuality]

class StillImageQuality(BaseModel):
    value: StillImageQualityValue
    ability: StillImageQualityAbility

    @model_validator(mode="after")
    def validate_ability(self):
        if self.value.raw not in self.ability.raw:
            raise ValueError("raw value must be one of the advertised abilities")

        if self.value.jpeg not in self.ability.jpeg:
            raise ValueError("jpeg value must be one of the advertised abilities")

        return self

class RangeAbility(BaseModel):
    min: int
    max: int
    step: int

class StillImageCompressionRation(BaseModel):
    value: int #Present value
    ability: RangeAbility #Ability values

    @model_validator(mode="after")
    def validate_value(self):
        minimum = self.ability.min
        maximum = self.ability.max
        step = self.ability.step

        if not minimum <= self.value <= maximum:
            raise ValueError("value is outside the supported range")

        if step <= 0 or (self.value - minimum) % step != 0:
            raise ValueError("value does not match the supported step")

        return self

HDRValue = Literal["pq", "off"]
class HDR(BaseModel):
    value: HDRValue #Present value
    ability: list[HDRValue] #Ability values

#4.9.21
