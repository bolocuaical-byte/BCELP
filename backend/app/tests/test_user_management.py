from typing import Dict

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def get_auth_token(email: str, password: str) -> str:
    response = client.post(
        "/auth/token",
        data={"username": email, "password": password},
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_user_crud_flow() -> None:
    new_user: Dict = {
        "email": "testuser@example.com",
        "full_name": "Test User",
        "password": "securepassword",
    }

    response = client.post("/auth/users", json=new_user)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["email"] == new_user["email"]

    token = get_auth_token(new_user["email"], new_user["password"])
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
    assert any(user["email"] == new_user["email"] for user in response.json())

    response = client.get(f"/users/{created_user['id']}", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == new_user["email"]

    response = client.put(
        f"/users/{created_user['id']}",
        json={"full_name": "Updated User"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["full_name"] == "Updated User"

    response = client.delete(f"/users/{created_user['id']}", headers=headers)
    assert response.status_code == 204

    response = client.get(f"/users/{created_user['id']}", headers=headers)
    assert response.status_code == 404


def test_role_permission_crud_flow() -> None:
    admin_user: Dict = {
        "email": "admin@example.com",
        "full_name": "Admin User",
        "password": "securepassword",
    }
    client.post("/auth/users", json=admin_user)
    token = get_auth_token(admin_user["email"], admin_user["password"])
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/roles/",
        json={"name": "admin", "description": "Administrator role"},
        headers=headers,
    )
    assert response.status_code == 201
    role = response.json()
    assert role["name"] == "admin"

    response = client.post(
        "/permissions/",
        json={"name": "manage_users", "description": "Manage user accounts"},
        headers=headers,
    )
    assert response.status_code == 201
    permission = response.json()
    assert permission["name"] == "manage_users"

    response = client.get(f"/roles/{role['id']}", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "admin"

    response = client.get(f"/permissions/{permission['id']}", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "manage_users"

    response = client.put(
        f"/roles/{role['id']}",
        json={"description": "Updated description"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["description"] == "Updated description"

    response = client.put(
        f"/permissions/{permission['id']}",
        json={"description": "Updated description"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["description"] == "Updated description"

    response = client.delete(f"/roles/{role['id']}", headers=headers)
    assert response.status_code == 204

    response = client.delete(f"/permissions/{permission['id']}", headers=headers)
    assert response.status_code == 204
