from canon_ccapi.models.devicestatus import StorageList
from canon_ccapi.models.devicestatus import CurrentStorage
from canon_ccapi.models.devicestatus import CurrentDirectory
from canon_ccapi.models.devicestatus import Battery
from canon_ccapi.models.devicestatus import BatteryList
from canon_ccapi.models.devicestatus import Lens
from canon_ccapi.models.devicestatus import PowerZoom
from canon_ccapi.models.devicestatus import Temperature


class DeviceStatusResource:
    def __init__(self, camera):
        self.camera = camera

    @property
    def storage(self) -> StorageList:
        return self.camera.devicestatus.storage

    @property
    def current_storage(self) -> CurrentStorage:
        return self.camera.devicestatus.current_storage 

    @property
    def current_directory(self) -> CurrentDirectory:
        return self.camera.devicestatus.current_directory

    @property
    def battery(self) -> Battery:
        return self.camera.devicestatus.battery

    @property
    def battery_list(self) -> BatteryList:
        return self.camera.devicestatus.battery_list

    @property
    def lens(self) -> Lens:
        return self.camera.devicestatus.lens

    @property
    def power_zoom(self) -> PowerZoom:
        return self.camera.devicestatus.power_zoom

    @property
    def temperature(self) -> Temperature:
        return self.camera.devicestatus.temperature
    
