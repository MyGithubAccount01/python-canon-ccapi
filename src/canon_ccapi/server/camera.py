from canon_ccapi.models.device import DeviceInformation

class VirtualCamera:

    def __init__(self):

        self.device_information = DeviceInformation(
            manufacturer="Canon",
            productname="EOS R5",
            guid="12345678",
            serialnumber="123456789",
            macaddress="00:00:00:00:00:00",
            firmwareversion="2.0.0",
        )

    def get_device_information(self):
        return {
            "manufacturer": "Canon",
            "productname": "Virtual Camera",
            "guid": "12345678",
            "serialnumber": "VIRTUAL001",
            "macaddress": "00:00:00:00:00:00",
            "firmwareversion": "1.0.0",
        }

    def get_device_information(self):
        return self.device_information