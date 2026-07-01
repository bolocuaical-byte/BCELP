from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def get_token(email: str, password: str):
    r = client.post("/auth/token", data={"username": email, "password": password})
    assert r.status_code == 200
    return r.json()["access_token"]


def test_research_group_and_line_flow():
    # create user
    user = {"email": "rm_user@example.com", "full_name": "RM User", "password": "pw"}
    r = client.post("/auth/users", json=user)
    assert r.status_code == 201
    token = get_token(user["email"], user["password"])
    headers = {"Authorization": f"Bearer {token}"}

    # create group
    r = client.post("/research-groups/", json={"name": "Group A", "description": "desc"}, headers=headers)
    assert r.status_code == 201
    group = r.json()

    # list groups
    r = client.get("/research-groups/", headers=headers)
    assert r.status_code == 200
    assert any(g["id"] == group["id"] for g in r.json())

    # create project
    r = client.post("/projects/", json={"name": "Proj A", "description": "pdesc"}, headers=headers)
    assert r.status_code == 201
    project = r.json()

    # create research line
    r = client.post("/research-lines/", json={"title": "Line 1", "summary": "s", "project_id": project["id"]}, headers=headers)
    assert r.status_code == 201
    rl = r.json()

    # get research line
    r = client.get(f"/research-lines/{rl['id']}", headers=headers)
    assert r.status_code == 200

    # cleanup
    r = client.delete(f"/research-lines/{rl['id']}", headers=headers)
    assert r.status_code == 204
    r = client.delete(f"/projects/{project['id']}", headers=headers)
    assert r.status_code == 204
    r = client.delete(f"/research-groups/{group['id']}", headers=headers)
    assert r.status_code == 204
