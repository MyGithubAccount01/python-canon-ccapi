#import json
#from pathlib import Path
#
#from canon_ccapi.models.device import DeviceInformation
#
#
#def load_device_information(path: Path) -> DeviceInformation:
#    with path.open("r", encoding="utf-8") as file:
#        data = json.load(file)
#
#    return DeviceInformation.model_validate(
#        data["device_information"]
#    )

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from canon_ccapi.models.device import DeviceInformation
from canon_ccapi.models.discovery import EndpointInfo


class CameraResources(BaseModel):
    device_information: DeviceInformation


class CameraProfile(BaseModel):
    endpoints: dict[str, list[EndpointInfo]]
    resources: CameraResources


def load_profile(path: Path) -> CameraProfile:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return CameraProfile.model_validate(data)