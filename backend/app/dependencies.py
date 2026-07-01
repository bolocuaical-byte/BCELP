from typing import Generator, List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.security import oauth2_scheme
from app.services.auth_service import AuthService
from app.db.session import get_db
from app.models.auth import User


def get_db_session() -> Generator:
    yield from get_db()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db_session),
) -> User:
    try:
        payload = AuthService.decode_access_token(token)
        user_id = payload.get("sub")
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    user = db.query(User).get(user_id)
    if not user or user.is_deleted:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found or inactive")
    return user


def require_roles(roles: List[str]):
    def _require(user: User = Depends(get_current_user)) -> User:
        user_role_names = [r.name for r in user.roles]
        for r in roles:
            if r not in user_role_names:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient privileges")
        return user

    return _require
