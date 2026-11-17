from fastapi import FastAPI, Request

from canon_ccapi.server.camera import VirtualCamera
from canon_ccapi.models.device import DeviceInformation
from canon_ccapi.models.discovery import (
    Discovery,
    EndpointInfo
)


camera = VirtualCamera()

app = FastAPI()


@app.get("/ccapi")
def discover(request: Request):

    base_url = str(request.base_url).rstrip("/")

    return {
        "ver100": [
            {
                "url": f"{base_url}/ccapi/ver100/deviceinformation",
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            }
        ]
    }


@app.get("/ccapi/ver100/deviceinformation")
def device_information():

    return camera.get_device_information()