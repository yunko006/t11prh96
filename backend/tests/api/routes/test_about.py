from fastapi.testclient import TestClient


def test_get_about(client: TestClient) -> None:
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"pseudo": "t11prh96"}
