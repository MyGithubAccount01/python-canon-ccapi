from unittest.mock import Mock
from canon_ccapi.client.client import CCAPIClient

def test_storage_v100():
    data = {
        "storagelist": [
            {
                "name": "sd",
                "url": "http://192.168.1.2:8080/ccapi/ver100/contents/sd",
                "accesscapability": "readwrite",
                "maxsize": 4016570368,
                "spacesize": 3800924160,
                "contentsnumber": 511,
            }
        ]
    }

    camera = CCAPIClient("192.168.1.100")

    camera._find_get_endpoint = Mock(return_value=Mock(
            url = "http://192.168.1.2:8080/ccapi/ver100/contents/sd",
            version="ver100"
        ))

    response = Mock()
    response.json.return_value = data 
    camera.client.get = Mock(return_value=response)

    storage = camera.get_storage_status()

#    response.raise_for_status.assert_called_once()

    #print(storage.storageList)

    assert storage.storageList[0].name == "sd"
    assert storage.storageList[0].contents_number == 511


def test_storage_v110():
    data = {
        "storagelist": [
            {
                "name": "cfex",
                "path": "/ccapi/ver110/contents/cfex",
                "accesscapability": "readonly",
                "maxsize": 4016570368,
                "spacesize": 3800924160,
                "contentsnumber": 511,
            }
        ]
    }

    camera = CCAPIClient("192.168.1.100")

    camera._find_get_endpoint = Mock(return_value=Mock(
            url = "http://192.168.1.2:8080/ccapi/ver110/contents/cfex",
            version="ver110"
        ))
    response = Mock()
    response.json.return_value = data 
    camera.client.get = Mock(return_value=response)

    storage = camera.get_storage_status()

    assert storage.storageList[0].name == "cfex"
    assert storage.storageList[0].path == "/ccapi/ver110/contents/cfex"
    assert storage.storageList[0].access_capability == "readonly"


def test_empty_storage():

    camera = CCAPIClient("192.168.1.100")
    camera._find_get_endpoint = Mock(return_value=Mock(
            url = "http://192.168.1.2:8080/ccapi/ver100/contents/sd",
            version="ver100"
        ))
    response = Mock()
    response.json.return_value = {"storagelist": []}
    camera.client.get = Mock(return_value=response)

    storage = camera.get_storage_status()

    assert storage.storageList == []