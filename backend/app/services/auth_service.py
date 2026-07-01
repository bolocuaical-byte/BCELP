from datetime import datetime, timedelta
from typing import Any

from jose import jwt

from app.core.config import settings


class AuthService:
    @staticmethod
    def create_access_token(subject: str) -> str:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.jwt_access_token_expires_minutes
        )
        payload = {
            "sub": subject,
            "exp": expire,
            "iat": datetime.utcnow(),
        }
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

    @staticmethod
    def decode_access_token(token: str) -> Any:
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
