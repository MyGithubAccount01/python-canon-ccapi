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



HDRValue = Literal["pq", "off"]
class HDR(BaseModel):
    value: HDRValue #Present value
    ability: list[HDRValue] #Ability values

#4.9.21
StillImageAspectRationValue = Literal["3:2", "x1.6","4:3", "16:9", "1:1"]
class StillImageAspectRation(BaseModel):
    value: StillImageAspectRationValue #Present value
    ability: list[StillImageAspectRationValue] #Ability values

FlashValue = Literal["auto", "on", "slowsynchro", "off"]
class Flash(BaseModel):
    value: FlashValue #Present value
    ability: list[FlashValue] #Ability values

MeteringModeValue = Literal["evaluative", "partial", "spot", "center_weighted_average"]
class MeteringMode(BaseModel):
    value: MeteringModeValue #Present value
    ability: list[MeteringModeValue] #Ability values

DriveModeValue = Literal[
    "single", #Single shooting
    "cont_super_hi", #High speed continuous +
    "highspeed", #High speed continuous
    "customhighspeedcont", #Custom high speed continuous
    "continuous", #Medium speed continuous
    "lowspeed", #Low speed continuous
    "silent", #Single Soft shooting
    "silent_single", #Soft contin shooting
    "silent_continuous", #Soft LS continuous
    "self_10sec", #Self-timer:10 sec
    "self_2sec", #Self-timer:2 sec
    "self_continuous", #Self-timer:Continuous
]
class DriveMode(BaseModel):
    value: DriveModeValue #Present value
    ability: list[DriveModeValue] #Ability values

ShootingSpeedValue = Literal[30,40,50,60,80,100,120,150,180,200]
class ShootingSpeed(BaseModel):
    value: ShootingSpeedValue #Present value
    ability: list[ShootingSpeedValue] #Ability values

ContinuousShootingNumberOfShotsValue = Literal[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
class ContinuousShootingNumberOfShots(BaseModel):
    value: ContinuousShootingNumberOfShotsValue #Present value
    ability: list[ContinuousShootingNumberOfShotsValue] #Ability values

AEBValue = Literal["+0.0",  # Exposure bracket value +0.0
                  "+0_1/3", # Exposure bracket value +0 1/3
                  "+0_2/3", # Exposure bracket value +0 2/3
                  "+1.0",   # Exposure bracket value +1.0
                  "+1_1/3", # Exposure bracket value +1 1/3
                  "+1_2/3", # Exposure bracket value +1 2/3
                  "+2.0"]   # Exposure bracket value +2.0
class AEB(BaseModel):
    value: AEBValue #Present value
    ability: list[AEBValue] #Ability values

class WBShiftValue(BaseModel):
    ba: int
    mg: int


class WBShiftAbility(BaseModel):
    ba: RangeAbility
    mg: RangeAbility


class WBShift(BaseModel):
    value: WBShiftValue
    ability: WBShiftAbility

    @model_validator(mode="after")
    def validate_values(self):
        for name in ("ba", "mg"):
            current = getattr(self.value, name)
            ability = getattr(self.ability, name)

            if not ability.min <= current <= ability.max:
                raise ValueError(f"{name} value is outside the supported range")

            if ability.step <= 0 or (current - ability.min) % ability.step != 0:
                raise ValueError(f"{name} value does not match the supported step")

        return self

WBBracketValue = Literal["0", "ba1", "ba2", "ba3", "mg1", "mg2", "mg3"]
class WBBracket(BaseModel):
    value: WBBracketValue #Present value
    ability: list[WBBracketValue] #Ability values

ColorSpaceValue = Literal["srgb", "adobe_rgb"]
class ColorSpace(BaseModel):
    value: ColorSpaceValue #Present value
    ability: list[ColorSpaceValue] #Ability values

PictureStyleKindValue = Literal["auto", "standard", "portrait", "landscape", "finedetail",
                                "neutral", "faithful", "monochrome", "userdef1", "userdef2", "userdef3"]
class PictureStyleKind(BaseModel):
    value: PictureStyleKindValue #Present value
    ability: list[PictureStyleKindValue] #Ability values

class PictureStyleValue(BaseModel):
    sharpness_strength: int
    sharpness_fineness: int
    sharpness_threshold: int
    contrast: int
    saturation: int
    colortone: int

class PictureStyleAbility(BaseModel):
    sharpness_strength: RangeAbility
    sharpness_fineness: RangeAbility
    sharpness_threshold: RangeAbility
    contrast: RangeAbility
    saturation: RangeAbility
    colortone: RangeAbility

class PictureStyle(BaseModel):
    value: PictureStyleValue
    ability: PictureStyleAbility

    @model_validator(mode="after")
    def validate_values(self):
        for name in PictureStyleValue.model_fields:
            current = getattr(self.value, name)
            ability = getattr(self.ability, name)

            if not ability.min <= current <= ability.max:
                raise ValueError(f"{name} is outside the supported range")

            if ability.step <= 0 or (current - ability.min) % ability.step != 0:
                raise ValueError(f"{name} does not match the supported step")

        return self

# TODO: Move this info to classes/client implementation
Sample = Literal["5472x2886_5994_raw_standard", #5472x2886 59.94fps RAW",
                 "4096x2160_5994_alli_standard_crop", #4096x2160 59.94fps For editing (ALL-I) Movie crop",
                 "1920x1080_2997_ipb_standard", #1920x1080 29.97fps Standard (IPB)",
                 "1920x1080_2500_ipb_light"] #1920x1080 25.00fps Light (IPB)"
ImageSize = Literal["4k", #3840x2160 (models with Digic8)
                   "fhd", #1920x1080 (models with Digic8)
                   "hd", #1280x720 (models with Digic8)
                   "8192x4320", #8192x4320
                   "7680x4320", #7680x4320
                   "6000x3164", #6000x3164
                   "5472x2886", #5472x2886
                   "4096x2160", #4096x2160
                   "3840x2160", #3840x2160
                   "1920x1080", #1920x1080
                   "rawsize", #RAW
                   "fullsize", #Fullsize (OpenGate ON)
                   "rawfullsize" #RAW + Fullsize
                  ]

FrameRate = Literal["17982", #179.82fps
    "15000", #150.00fps
    "11988", #119.9fps
    "10000", #100.0fps
    "5994", #59.94fps
    "5000", #50.00fps
    "2997", #29.97fps
    "2500", #25.00fps
    "2400", #24.00fps
    "2398" #23.98fps
    ]

Compression = Literal["raw", #RAW
    "alli", #ALL-I
    "ipb", #IPB
    "longgop", #Long GOP
    "intra" #Intra-frame
]

MovieMode = Literal[
    "crop", #Movie cropping
    "fine" #Fine Movie
]
#########


class PowerZoomValue(BaseModel):
    speed: Literal["slow", "fast"]
    level: int


class PowerZoomAbility(BaseModel):
    speed: list[Literal["slow", "fast"]]
    level: RangeAbility

class PowerZoom(BaseModel):
    value: PowerZoomValue
    ability: PowerZoomAbility

    @model_validator(mode="after")
    def validate_values(self):
        if self.value.speed not in self.ability.speed:
            raise ValueError("Unsupported zoom speed")

        minimum = self.ability.level.min
        maximum = self.ability.level.max
        step = self.ability.level.step

        if not minimum <= self.value.level <= maximum:
            raise ValueError("Zoom level outside supported range")

        if step <= 0 or (self.value.level - minimum) % step != 0:
            raise ValueError("Zoom level does not match supported step")

        return self

