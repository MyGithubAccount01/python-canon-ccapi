from urllib import response

import httpx

from canon_ccapi.models.device import DeviceInformation
from canon_ccapi.models.discovery import Discovery, EndpointInfo
from canon_ccapi.models.devicestatus import Storage
from urllib.parse import urlsplit
from dataclasses import dataclass
from canon_ccapi.protocol.normalizers.devicestatus import (
    normalize_storage_status,
)

@dataclass
class DiscoveredEndpoint:
    version: str
    url: str

class CCAPIClient:
    def __init__(self, host: str, port: int = 8080):
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}/ccapi"
        self.client = httpx.Client(timeout=10.0)

        self.discovery = None

    def connect(self):
        response = httpx.get(self.base_url, timeout=10.0)
        response.raise_for_status()

        self.discovery = Discovery.model_validate(response.json())

        return self.discovery
    
#    def connect(self):
#        response = self.client.get(f"{self.base_url}")
#        response.raise_for_status()
#        
#        self.discovery = Discovery.model_validate(response.json())
#
#        return self.discovery

    def get(self, endpoint: str):
        response = self.client.get(
            f"{self.base_url}:{self.port}/{endpoint}"
        )
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict):
        response = self.http.post(
            f"{self.base_url}{endpoint}",
            json=data
        )
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict):
        response = self.http.put(
            f"{self.base_url}{endpoint}",
            json=data
        )
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str):
        response = self.http.delete(
            f"{self.base_url}{endpoint}"
        )
        response.raise_for_status()
        return response.json()

    def close(self):
        self.http.close()

    def get_device_information(self) -> DeviceInformation:
        response = self.client.get(
            f"{self.base_url}/ver100/deviceinformation"
        )
        response.raise_for_status()
    
        return DeviceInformation.model_validate(response.json())

    def get_storage_status(self) -> Storage:
        endpoint = self._find_get_endpoint("/devicestatus/storage")

        response = self.client.get(endpoint.url)
        response.raise_for_status()

        return normalize_storage_status(
            endpoint.version,
            response.json(),
        )

    def _find_get_endpoint(self, resource: str) -> DiscoveredEndpoint:
        if self.discovery is None:
            raise RuntimeError("Call connect() first")
    
        for version, endpoints in self.discovery.root.items():
            for endpoint in endpoints:
                path = urlsplit(endpoint.url).path
    
                if path.endswith(resource) and endpoint.get:
                    base_path = urlsplit(self.base_url).path.rstrip("/")
    
                    if not path.startswith(base_path + "/"):
                        raise ValueError(
                            f"Unexpected endpoint path: {path}"
                        )
    
                    relative_path = path[len(base_path):]
    
                    url = self.base_url.rstrip("/") + relative_path
    
                    return DiscoveredEndpoint(
                        version=version,
                        url=url,
                    )
    
        raise LookupError(f"No GET endpoint found for {resource}")

    def _resolve_endpoint(self, endpoint: EndpointInfo) -> str:
        if endpoint.path:
            return f"http://{self.host}:{self.port}{endpoint.path}"
    
        if endpoint.url:
            parsed = urlsplit(endpoint.url)
            return f"http://{self.host}:{self.port}{parsed.path}"
    
        raise ValueError("Discovery endpoint has neither url nor path")