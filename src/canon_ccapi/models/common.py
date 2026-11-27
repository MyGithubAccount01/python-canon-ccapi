from pydantic import BaseModel, Field, model_validator
from typing import Literal

#4.9.57, 4.9.61, 4.9.64, 4.9.65, 4.9.66, 4.9.67, 4.9.68, 4.9.77
class StringSetting(BaseModel):
    value: str
    ability: list[str]

    @model_validator(mode="after")
    def validate_value(self):
        if self.value not in self.ability:
            raise ValueError("value must be one of the advertised abilities")
        return self

#4.9.46, 4.9.47, 4.9.52, 4.9.53, 4.9.54, 4.9.59, 4.9.60, 4.9.72, 4.9.73, 4.9.75
# TODO: This becomes StringSetting

EnableDisable = Literal["enable", "disable"]
class EnableDisableModel(BaseModel):
    value: EnableDisable #Present value
    ability: list[EnableDisable] #Ability values

    @model_validator(mode="after")
    def validate_value(self):
        if self.value not in self.ability:
            raise ValueError("value must be one of the advertised abilities")
        return self

#4.9.19, 4.9.49, 4.9.50, 4.9.51, 4.9.55, 4.9.63, 4.9.69, 4.9.70, 4.9.71
class RangeAbility(BaseModel):
    min: int
    max: int
    step: int

class RangedSetting(BaseModel):
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

class StringName(BaseModel):
    name: str #Name of the string setting