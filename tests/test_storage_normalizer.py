from canon_ccapi.protocol.normalizers.devicestatus import (
    normalize_storage_status,
)


def test_normalize_storage_v100():
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

    result = normalize_storage_status("ver100", data)

    assert len(result.storageList) == 1

    storage = result.storageList[0]

    assert storage.name == "sd"
    assert storage.access_capability == "readwrite"
    assert storage.contents_path.endswith("/contents/sd")


def test_normalize_storage_v110():
    data = {
        "storagelist": [
            {
                "name": "card1",
                "path": "/ccapi/ver110/contents/card1",
                "accesscapability": "readonly",
                "maxsize": 4016570368,
                "spacesize": 3800924160,
                "contentsnumber": 511,
            }
        ]
    }

    result = normalize_storage_status("ver110", data)

    storage = result.storageList[0]

    assert storage.name == "card1"
    assert storage.contents_path == "/ccapi/ver110/contents/card1"
    assert storage.access_capability == "readonly"


def test_normalize_empty_storage():
    result = normalize_storage_status(
        "ver100",
        {"storagelist": []},
    )

    assert result.storageList == []