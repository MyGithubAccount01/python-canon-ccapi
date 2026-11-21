from pydantic import BaseModel
from typing import Literal
from canon_ccapi.models.discovery import EndpointInfo

DisplayOffValue = Literal["10", "20", "30", "60", "120", "180"]
BeepValue = Literal["enable", "disable", "disabletouch"]
AutoPowerOffValue = Literal["30", "60", "120", "180", "300", "600", "disable", "immediately"]
NetworkConnectionAction = Literal["disconnect", "reboot"]
NetworkConnectionSettings = Literal["set01", "set02", "set03", "set04", "set05", 
                                    "set06", "set07", "set08", "set09", "set10", 
                                    "set11", "set12", "set13", "set14", "set15", 
                                    "set16", "set17", "set18", "set19", "set20"]

LANType = Literal["ether", "wft", "wifi"]
Method = Literal["infrastructure", "cameraap"]
Channel = Literal["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                  "11", "12", "13", "36", "40", "44", "48", "149", "153", 
                  "157", "161", "165"]
Authentication = Literal["open", "sharedkey", "wpawpa2psk", "wpawpa2enterprize",
                          "wpa2wpa3personal", "wpawpa2wpa3personal", "wpawpa2wpa3enterprize"]
Encryption = Literal["none", "wep", "tkipaes", "aes"]
KeyIndex = Literal["1", "2", "3", "4"]
IPV4AddressSet = Literal["auto", "manual"]
UseIPv6 = Literal["disable", "enable"]
IPV6ManualSetting = Literal["disable", "enable"]

class DateTime (BaseModel):
    date_time: str #Function datetime
    dst: bool #Daylight saving time flag

class CardFormat(BaseModel):
    name: str #Card name

class Beep(BaseModel):
    value: BeepValue #Present value
    ability: list[BeepValue] #List of supported values

class DisplayOff(BaseModel):
    value: DisplayOffValue #Present value
    ability: list[DisplayOffValue] #List of supported values

class AutoPowerOff(BaseModel):
    value: AutoPowerOffValue #Present value
    ability: list[AutoPowerOffValue] #List of supported values

class SensorCleaning(BaseModel):
    auto_power_off: bool #Whether to perform auto power-off after sensor cleaning

class NetworkConnection(BaseModel):
    action: NetworkConnectionAction #Communication connection operation

"""This gets a list of the Network setting APIs supported by the Canon camera.
In case of a Canon camer that only supports Wi-Fi, this API is not supported. 
Check the Canon camera used."""
class NetworkSetting(RootModel[dict[str, list[EndpointInfo]]]):
    pass

"""This gets the connection settings (SET) that are currently running and that can be changed.
The only connection settings (SET) that can be changed are those initiated by CCAPI.
In case of a Canon camera that only support Wi-Fi, this API is not supported. Check the Canon
camera used."""
class CurrentConnectionSetting(BaseModel):
    value: NetworkConnectionSettings #Present value
    ability: list[NetworkConnectionSettings] #Ability values

"""This gets the list of connection setting (SET) information saved in the Canon camera."""
class ConnectionSetting(BaseModel):
    commsetting: list[str]
    functionsetting: list[str]

class ConnectionSettingList(RootModel[dict[str, ConnectionSetting]]):
    pass

class CommunicationSetting(BaseModel):
    lantype: LANType #LAN type
    ssid: str #SSID of the network
    method: Method #Connection method
    channel: Channel #Channel of the network
    authentication: Authentication #Authentication method
    encryption: Encryption #Encryption method
    keyindex: KeyIndex #Key index
    password: str #Password for the network
    ipv_ipaddressset: IPV4AddressSet #IP address setting
    ipv4_ipaddress: str #IP address
    ipv4_subnetmask: str #Subnet mask
    ipv4_gateway: str #Gateway
    ipv6_useipv6: UseIPv6 #Use IPv6
    ipv6_manual_setting: IPV6ManualSetting #Manual setting for IPv6
    ipv6_manual_address: str #Manual IPv6 address
    ipv6_prefixlength: str #Prefix length
    ipv6_gateway: str #Gateway