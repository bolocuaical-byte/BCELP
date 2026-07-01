from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def get_token(email: str, password: str):
    r = client.post("/auth/token", data={"username": email, "password": password})
    assert r.status_code == 200
    return r.json()["access_token"]


def test_equipment_crud_flow():
    user = {"email": "lab_user@example.com", "full_name": "Lab User", "password": "pw"}
    r = client.post("/auth/users", json=user)
    assert r.status_code == 201
    token = get_token(user["email"], user["password"])
    headers = {"Authorization": f"Bearer {token}"}

    # create equipment
    eq_in = {"name": "Oscilloscope", "serial_number": "OSC-1234", "model": "X1000", "manufacturer": "Acme", "location": "Lab A", "description": "Test scope"}
    r = client.post("/equipment/", json=eq_in, headers=headers)
    assert r.status_code == 201
    eq = r.json()

    # get equipment
    r = client.get(f"/equipment/{eq['id']}")
    assert r.status_code == 200

    # list equipment
    r = client.get("/equipment/")
    assert r.status_code == 200

    # update
    r = client.put(f"/equipment/{eq['id']}", json={"location": "Lab B"})
    assert r.status_code == 200
    assert r.json()["location"] == "Lab B"

    # delete
    r = client.delete(f"/equipment/{eq['id']}")
    assert r.status_code == 204
