from pydantic import BaseModel, RootModel

class EndpointInfo(BaseModel):
    url: str | None = None
    path: str | None = None
    get: bool = False
    post: bool = False
    put: bool = False
    delete: bool = False

class Discovery(RootModel[dict[str, list[EndpointInfo]]]):
    pass

#import json
#
#from canon_ccapi.models.discovery import DiscoveryDocument
#
#with open("discovery.json") as f:
#    raw_data = json.load(f)
#
#discovery = DiscoveryDocument.model_validate(raw_data)
#
#for endpoint in discovery.ver100:
#    print(endpoint.url)
#    print("GET:", endpoint.get)
#
#http://192.168.1.2:8080/ccapi/ver100/deviceinformation
#GET: True