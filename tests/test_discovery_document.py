from canon_ccapi.models.discovery import Discovery

def test_discovery():

    data = {
        "ver100": [
            {
                "url": "http://camera/ccapi/ver100/deviceinformation",
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            }
        ]
    }

    discovery = Discovery.model_validate(data)

    assert len(discovery.root["ver100"]) == 1
    assert discovery.root["ver100"][0].get is True
    assert discovery.root["ver100"][0].post is False
    assert discovery.root["ver100"][0].put is False
    assert discovery.root["ver100"][0].delete is False