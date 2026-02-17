from fastapi.testclient import TestClient
from app.schemas.about import About

me_test = About(
    nom="prh",
    prenom="tom",
    role="backend dev",
    description="bonjour ceci est un test de desc",
)


def test_get_about(client: TestClient) -> None:
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == me_test.model_dump()
