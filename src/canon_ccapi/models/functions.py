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
CommFunction = Literal["unspecified", "ccapi", "eos_utility", "browserremote", "ftp_trans", "smartphone"]
CORSSettingValue = Literal["enable", "disable"]
StillMovieSeparateValue = Literal["enable", "disable"]
RecordOptions = Literal["standard", "auto_switch_card", "rec_separately", "rec_to_multiple"]
StorageOptions = Literal["none", "card1", "card2"]
FanModeOptions = Literal["auto", "standby", "on", "off"]
FanSpeedOptions = Literal["high", "middle", "low", "stop"]
ConnectSettingAuthentication = Literal["open", "enhanced_open", "wpawpa2wpa3personal", "wpawpa2enterprise", "wpa3enterprise192bit", "wpa2wpa3personal"]
ScreenDimmerValue = Literal["5", "10", "15", "20", "25", "30", "disable"]
ViewFinderValue = Literal["1", "3", "off"]

WIFIConnectionAction = Literal["disconnect"]

class DateTime (BaseModel):
    date_time: str #Function datetime
    dst: bool #Daylight saving time flag

class CardFormat(BaseModel):
    name: str #Card name

class SensorCleaning(BaseModel):
    auto_power_off: bool #Whether to perform auto power-off after sensor cleaning

class NetworkConnection(BaseModel):
    action: NetworkConnectionAction #Communication connection operation

"""This gets a list of the Network setting APIs supported by the Canon camera.
In case of a Canon camer that only supports Wi-Fi, this API is not supported. 
Check the Canon camera used."""
class NetworkSetting(RootModel[dict[str, list[EndpointInfo]]]):
    pass

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

class FunctionSetting(BaseModel):
    commfunction: CommFunction #Communication function

class FunctionSettingList(RootModel[dict[str, FunctionSetting]]):
    pass

class WIFIConnection(BaseModel):
    action: WIFIConnectionAction #Wi-Fi disconnect operation
    
class WIFISetting(BaseModel):
    ssid: str #SSID of the network
    method: Method #Connection method
    channel: Channel #Channel of the network
    authentication: Authentication #Authentication method
    encryption: Encryption #Encryption method
    keyindex: KeyIndex #Key index
    password: str #Password for the network
    ipaddressset: IPAddressSet #IP address setting
    ipaddress: str #IP address
    subnetmask: str #Subnet mask
    gateway: str #Gateway

class WIFISettingList(RootModel[dict[str, WIFISetting]]):
    pass

class CommonName(BaseModel):
    commonname: str #Common name


class CORSOrigin(BaseModel):
    origin: str #CORS origin

class ConnectSetting(BaseModel):
    lantype: str #LAN type
    ssid: str #SSID of the network
    method: Method #Connection method
    channel: Channel #Channel of the network
    authentication: ConnectSettingAuthentication #Authentication method
    password: str #Password for the network
    ipv4_ipaddressset: IPV4AddressSet #IP address setting
    ipv4_ipaddress: str #IP address
    ipv4_subnetmask: str #Subnet mask
    ipv4_gateway: str #Gateway
    ipv6_useipv6: UseIPv6 #Use IPv6
    ipv6_manual_setting: IPV6ManualSetting #Manual IPv6 setting
    ipv6_ipaddress: str #IPv6 address
    ipv6_prefixlength: str #IPv6 prefix length
    ipv6_gateway: str #IPv6 gateway
    ether: str #Ethernet setting
    wifi: str #Wi-Fi setting

class CreateDirectory(BaseModel):
    directoryname: str #Directory name

class FilenameUsersetting1(BaseModel):
    usersetting1: str #User setting 1

class FilenameUsersetting1(BaseModel):
    usersetting2: str #User setting 1

class MovineIndex(BaseModel):
    index: str #Movie index

class MoveNameUserDefined(BaseModel):
    userdefined: str #User defined move name

