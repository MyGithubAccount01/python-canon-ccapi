# Python Library for Canon CCAPI

This library is designed to be a comprehensive library to communicate with Canon cameras via the CCAPI built-in. 

## Adding Endpoints to the Library

A practical rule for adding endpoints
I'd use this decision process every time you add one:
1. Does the endpoint exist in multiple CCAPI versions?
   
   If not, implement only the version that exists.
2. Does its response differ between versions?
   
   If yes, use separate version-specific wire models.
3. Do you need one consistent representation across versions?
   
   If yes, add a normalized model and normalizer.
4. Does the server need to expose this endpoint?
   
   Implement the corresponding server handler and make discovery advertise it.
5. Add tests.
   
   Test parsing the response, client behavior, and server response as appropriate.


## How Data Models Work


Let's walk through it using your soundrecording endpoint as well.
1. The model describes the response
You define this once:
'''
class StringSetting(BaseModel):
    value: str
    ability: list[str]

    @model_validator(mode="after")
    def validate_value(self):
        if self.value not in self.ability:
            raise ValueError("value must be one of the advertised abilities")
        return self
'''

Both framerate and soundrecording can use this model.
2. The GET method asks the camera what it supports
Imagine your resource class has a method like this:

'''
def get_sound_recording(self) -> StringSetting:
    response = self.camera.get(
        "shooting/settings/soundrecording"
    )

    return StringSetting.model_validate(response)
'''

The important line is:

'''
return StringSetting.model_validate(response)
'''

This takes the JSON returned by the camera and turns it into a validated Pydantic object.

For example:

'''
sound_recording = camera.shooting.get_sound_recording()

print(sound_recording.value)
# auto

print(sound_recording.ability)
# ['auto', 'manual', 'disable']
'''

The camera supplies the ability list. Your model validates its structure and ensures the current value is in that list.
3. The SET method uses that information
Now you can implement:

'''
def set_sound_recording(self, value: str):
    current = self.get_sound_recording()

    if value not in current.ability:
        raise ValueError(
            f"Unsupported sound recording setting: {value}"
        )

    self.camera.put(
        "shooting/settings/soundrecording",
        {"value": value}
    )
'''

The sequence is:
1. GET the current sound recording settings.
2. Validate the response using StringSetting.
3. Read the camera's advertised ability list.
4. Check the requested value against that list.
5. PUT the requested value if supported.
4. Apply the same approach to framerate
You can use the exact same model and validation approach:

'''
def get_framerate(self) -> StringSetting:
    response = self.camera.get(
        "shooting/settings/moviequality/framerate"
    )
    return StringSetting.model_validate(response)


def set_framerate(self, value: str):
    current = self.get_framerate()

    if value not in current.ability:
        raise ValueError(f"Unsupported framerate: {value}")

    self.camera.put(
        "shooting/settings/moviequality/framerate",
        {"value": value}
    )
'''

### One architectural suggestion

Eventually, you may notice that many of your SET methods repeat the same validation logic. That's a good candidate for a shared helper.

For now, though, I'd keep the GET and SET methods explicit. You're still building out the resource layer, and seeing the request/validation/response sequence clearly is more valuable than abstracting it prematurely.

The key concept is that StringSetting doesn't know what the camera supports. The GET request retrieves that information, and the model validates and exposes it.
