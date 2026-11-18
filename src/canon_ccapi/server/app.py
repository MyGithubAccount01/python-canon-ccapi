#from fastapi import FastAPI, Request
#
#from canon_ccapi.server.camera import VirtualCamera
#from canon_ccapi.models.device import DeviceInformation
#from canon_ccapi.models.discovery import (
#    Discovery,
#    EndpointInfo
#)
#from pathlib import Path
#from canon_ccapi.server.profile import load_device_information
#
#
###################################
#
#PROFILE_PATH = (
#    Path(__file__).parent.parent.parent.parent
#    / "profiles"
#    / "eos_r5.json"
#)
#
#device_information = load_device_information(PROFILE_PATH)
#camera = VirtualCamera(device_information)
#
#app = FastAPI()
#
#
#@app.get("/ccapi")
#def discover(request: Request):
#
#    base_url = str(request.base_url).rstrip("/")
#
#    return {
#        "ver100": [
#            {
#                "url": f"{base_url}/ccapi/ver100/deviceinformation",
#                "get": True,
#                "post": False,
#                "put": False,
#                "delete": False
#            }
#        ]
#    }
#
#
#@app.get("/ccapi/ver100/deviceinformation")
#def device_information():
#
#    return camera.get_device_information()

from pathlib import Path
from urllib.parse import urlsplit

from fastapi import FastAPI, Request, HTTPException

from canon_ccapi.server.camera import VirtualCamera
from canon_ccapi.server.profile import load_profile


PROFILE_PATH = (
    Path(__file__).parent.parent.parent.parent
    / "profiles"
    / "eos_r5.json"
)

profile = load_profile(PROFILE_PATH)
camera = VirtualCamera(profile)

app = FastAPI()


@app.get("/ccapi")
def discover(request: Request):

    base_url = str(request.base_url).rstrip("/")
    discovery = {}

    for version, endpoints in camera.get_endpoints().items():

        discovery[version] = []

        for endpoint in endpoints:

            entry = endpoint.model_dump(exclude_none=True)

            # Absolute URL format (EOS RP)
            if endpoint.url is not None:
                path = urlsplit(endpoint.url).path
                entry["url"] = f"{base_url}{path}"

            # Relative path format (EOS R5)
            # No transformation needed.

            discovery[version].append(entry)

    return discovery


@app.get("/ccapi/{version}/deviceinformation")
def device_information(version: str):
    endpoint_path = f"/ccapi/{version}/deviceinformation"

    # Inside device_information:
    endpoints = camera.get_endpoints().get(version, [])
    supported = any(
        endpoint.get
        and (endpoint.path or endpoint.url)
        and urlsplit(endpoint.path or endpoint.url).path == endpoint_path
        for endpoint in endpoints
    )
    if not supported:
        raise HTTPException(status_code=404, detail="Endpoint not found")

    return camera.device_information