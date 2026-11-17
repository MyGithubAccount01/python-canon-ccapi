from canon_ccapi.client.client import CCAPIClient
from canon_ccapi.models.discovery import Discovery

#camera = CCAPIClient(host="192.168.20.218")
camera = CCAPIClient(host="192.168.20.214")

discovery = camera.connect()

device = camera.get_device_information()
print(device.manufacturer)
print(device.productname)
print(device.serialnumber)

def discover_endpoints(discovery: Discovery):
    for version, endpoints in discovery.root.items():
        print(f"CCAPI version: {version}")
    
        for endpoint in endpoints:
            print(endpoint.url)



#discovery = camera.connect()
#
#print("Available endpoints:")
#
#for endpoint in discovery.ver100:
#    print(endpoint.url)
#
#info = camera.get_device_information()
#
#print(info)
#
#camera.close()