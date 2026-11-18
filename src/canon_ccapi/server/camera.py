from canon_ccapi.server.profile import CameraProfile
from canon_ccapi.models.device import DeviceInformation

class VirtualCamera:

    def __init__(self, profile: CameraProfile):
        #self.device_information = device_information
        self.profile = profile

    @property
    def device_information(self) -> DeviceInformation:
        return self.profile.resources.device_information

#    @device_information.setter
#    def device_information(self, value: DeviceInformation) -> None:
#        self.profile.resources.device_information = value

#    def get_device_information(self):
#        return self.device_information

    def get_endpoints(self):
        return self.profile.endpoints