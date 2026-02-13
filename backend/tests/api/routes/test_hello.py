from fastapi.testclient import TestClient


def test_get_hello(client: TestClient) -> None:
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}
