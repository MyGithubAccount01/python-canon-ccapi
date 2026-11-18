from canon_ccapi.client.client import CCAPIClient
from canon_ccapi.models.discovery import EndpointInfo


CAMERA_HOST = "192.168.20.218"
CAMERA_PORT = 8080

EXPECTED_URL = (
    "http://192.168.20.218:8080"
    "/ccapi/ver100/deviceinformation"
)


def test_resolve_absolute_url():
    """EOS RP-style discovery response."""

    camera = CCAPIClient(
        host=CAMERA_HOST,
        port=CAMERA_PORT,
    )

    endpoint = EndpointInfo(
        url="http://192.168.20.218:8080/ccapi/ver100/deviceinformation",
        get=True,
    )

    result = camera._resolve_endpoint(endpoint)

    assert result == EXPECTED_URL


def test_resolve_relative_path():
    """EOS R5-style discovery response."""

    camera = CCAPIClient(
        host=CAMERA_HOST,
        port=CAMERA_PORT,
    )

    endpoint = EndpointInfo(
        path="/ccapi/ver100/deviceinformation",
        get=True,
    )

    result = camera._resolve_endpoint(endpoint)

    assert result == EXPECTED_URL