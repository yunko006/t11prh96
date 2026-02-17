import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def reset_projects_store():
    """Reset the in-memory store and ID counter before each test."""
    import app.api.routes.projects as projects_module
    projects_module.projects_db.clear()
    projects_module._next_id = 1
    yield
    projects_module.projects_db.clear()
    projects_module._next_id = 1


def test_get_all_projects_empty(client: TestClient) -> None:
    response = client.get("/projects")
    assert response.status_code == 200
    assert response.json() == []


def test_create_project(client: TestClient) -> None:
    payload = {"name": "My Project", "description": "A test project"}
    response = client.post("/projects", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "My Project"
    assert data["description"] == "A test project"


def test_create_project_without_description(client: TestClient) -> None:
    payload = {"name": "Minimal Project"}
    response = client.post("/projects", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Minimal Project"
    assert data["description"] is None


def test_create_project_missing_name(client: TestClient) -> None:
    response = client.post("/projects", json={"description": "no name"})
    assert response.status_code == 422


def test_get_all_projects(client: TestClient) -> None:
    client.post("/projects", json={"name": "Project A"})
    client.post("/projects", json={"name": "Project B"})
    response = client.get("/projects")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Project A"
    assert data[1]["name"] == "Project B"


def test_get_one_project(client: TestClient) -> None:
    client.post("/projects", json={"name": "My Project"})
    response = client.get("/projects/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "My Project"


def test_get_one_project_not_found(client: TestClient) -> None:
    response = client.get("/projects/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"


def test_update_project(client: TestClient) -> None:
    client.post("/projects", json={"name": "Old Name", "description": "Old desc"})
    payload = {"name": "New Name", "description": "New desc"}
    response = client.put("/projects/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "New Name"
    assert data["description"] == "New desc"


def test_update_project_partial(client: TestClient) -> None:
    client.post("/projects", json={"name": "Original", "description": "Keep this"})
    response = client.put("/projects/1", json={"name": "Updated"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated"
    assert data["description"] == "Keep this"


def test_update_project_not_found(client: TestClient) -> None:
    response = client.put("/projects/999", json={"name": "Ghost"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"


def test_delete_project(client: TestClient) -> None:
    client.post("/projects", json={"name": "To Delete"})
    response = client.delete("/projects/1")
    assert response.status_code == 204
    get_response = client.get("/projects/1")
    assert get_response.status_code == 404


def test_delete_project_not_found(client: TestClient) -> None:
    response = client.delete("/projects/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"


def test_ids_are_unique_and_incremental(client: TestClient) -> None:
    r1 = client.post("/projects", json={"name": "First"})
    r2 = client.post("/projects", json={"name": "Second"})
    assert r1.json()["id"] == 1
    assert r2.json()["id"] == 2
