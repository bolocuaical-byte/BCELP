import hashlib
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.auth import RefreshToken


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(subject: str, roles: Optional[List[str]] = None) -> str:
        expire = datetime.utcnow() + timedelta(minutes=settings.jwt_access_token_expires_minutes)
        payload: Dict[str, Any] = {
            "sub": str(subject),
            "exp": expire,
            "iat": datetime.utcnow(),
        }
        if roles:
            payload["roles"] = roles
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

    @staticmethod
    def decode_access_token(token: str) -> Dict[str, Any]:
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])

    @staticmethod
    def create_refresh_token(user_id: str) -> str:
        raw = str(uuid.uuid4())
        hashed = hashlib.sha256(raw.encode()).hexdigest()
        # persist hashed token
        db = SessionLocal()
        try:
            rt = RefreshToken(token_hash=hashed, user_id=user_id)
            db.add(rt)
            db.commit()
            db.refresh(rt)
        finally:
            db.close()
        return raw

    @staticmethod
    def verify_refresh_token(raw_token: str) -> Optional[RefreshToken]:
        hashed = hashlib.sha256(raw_token.encode()).hexdigest()
        db = SessionLocal()
        try:
            rt = db.query(RefreshToken).filter(RefreshToken.token_hash == hashed, RefreshToken.revoked == False).one_or_none()
            return rt
        finally:
            db.close()

    @staticmethod
    def revoke_refresh_token(rt: RefreshToken) -> None:
        db = SessionLocal()
        try:
            db_token = db.query(RefreshToken).get(rt.id)
            if db_token:
                db_token.revoked = True
                db.commit()
        finally:
            db.close()
