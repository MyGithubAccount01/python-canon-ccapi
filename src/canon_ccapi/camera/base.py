from canon_ccapi.models.device import DeviceInformation
from canon_ccapi.resources.devicestatus import DeviceStatusResource


class BaseCamera:
    def __init__(self):
        self.devicestatus = DeviceStatusResource(self)
        

    @property
    def device_information(self) -> DeviceInformation:
        return self.profile.resources.device_information

#    @device_information.setter
#    def device_information(self, value: DeviceInformation) -> None:
#        self.profile.resources.device_information = value

