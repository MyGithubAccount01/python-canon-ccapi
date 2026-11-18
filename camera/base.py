from canon_ccapi.models.device import DeviceInformation


class BaseCamera:
    def __init__(self):
        pass

    @property
    def device_information(self) -> DeviceInformation:
        return self.profile.resources.device_information

#    @device_information.setter
#    def device_information(self, value: DeviceInformation) -> None:
#        self.profile.resources.device_information = value