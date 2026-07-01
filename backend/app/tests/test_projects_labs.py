from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_projects_crud_flow():
    # create a user first to be owner
    new_user = {"email": "projuser@example.com", "full_name": "Proj User", "password": "pw"}
    r = client.post("/auth/users", json=new_user)
    assert r.status_code == 201
    created = r.json()

    # get token
    r = client.post("/auth/token", data={"username": new_user["email"], "password": new_user["password"]})
    assert r.status_code == 200
    token = r.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # create project
    r = client.post("/projects/", json={"name": "Test Project", "description": "desc"}, headers=headers)
    assert r.status_code == 201
    proj = r.json()

    # list
    r = client.get("/projects/", headers=headers)
    assert r.status_code == 200
    assert any(p["id"] == proj["id"] for p in r.json())

    # get
    r = client.get(f"/projects/{proj['id']}", headers=headers)
    assert r.status_code == 200

    # update
    r = client.put(f"/projects/{proj['id']}", json={"description": "updated"}, headers=headers)
    assert r.status_code == 200
    assert r.json()["description"] == "updated"

    # delete
    r = client.delete(f"/projects/{proj['id']}", headers=headers)
    assert r.status_code == 204


def test_labs_crud_flow():
    new_user = {"email": "labuser@example.com", "full_name": "Lab User", "password": "pw"}
    r = client.post("/auth/users", json=new_user)
    assert r.status_code == 201
    r = client.post("/auth/token", data={"username": new_user["email"], "password": new_user["password"]})
    assert r.status_code == 200
    token = r.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    r = client.post("/labs/", json={"name": "Test Lab", "location": "Building A"}, headers=headers)
    assert r.status_code == 201
    lab = r.json()

    r = client.get("/labs/", headers=headers)
    assert r.status_code == 200

    r = client.get(f"/labs/{lab['id']}", headers=headers)
    assert r.status_code == 200

    r = client.put(f"/labs/{lab['id']}", json={"description": "updated"}, headers=headers)
    assert r.status_code == 200
    assert r.json()["description"] == "updated"

    r = client.delete(f"/labs/{lab['id']}", headers=headers)
    assert r.status_code == 204
