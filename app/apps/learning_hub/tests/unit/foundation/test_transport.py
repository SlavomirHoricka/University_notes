import httpx


def test_provider_failure_transport_is_test_only(test_transport: httpx.MockTransport) -> None:
    with httpx.Client(transport=test_transport) as client:
        response = client.get("https://fixture.invalid/status")
    assert response.status_code == 503
    assert response.json() == {"fixture": "unavailable"}
