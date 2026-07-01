from app.services.auth_service import AuthService


def test_password_hash_and_verify():
    pw = "s3cret!"
    h = AuthService.get_password_hash(pw)
    assert AuthService.verify_password(pw, h)


def test_jwt_roundtrip():
    token = AuthService.create_access_token("user-id-123", roles=["admin"])
    payload = AuthService.decode_access_token(token)
    assert payload.get("sub") == "user-id-123"
    assert "roles" in payload
