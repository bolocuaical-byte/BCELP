from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import Token, TokenRefresh, LoginRequest
from app.schemas.user import UserCreate, UserRead
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.dependencies import get_db_session, get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db = next(get_db_session())
    user = UserService.get_by_email(db, form_data.username)
    if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    roles = [r.name for r in user.roles]
    access_token = AuthService.create_access_token(str(user.id), roles=roles)
    refresh_token = AuthService.create_refresh_token(str(user.id))
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}


@router.post("/refresh", response_model=TokenRefresh)
def refresh_token(payload: TokenRefresh):
    rt = AuthService.verify_refresh_token(payload.refresh_token)
    if not rt:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    access_token = AuthService.create_access_token(str(rt.user_id))
    # optionally revoke and create new refresh token
    return {"access_token": access_token}


@router.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate):
    db = next(get_db_session())
    user = UserService.create(db, user_in)
    return user


@router.get("/me", response_model=UserRead)
def read_me(current_user: Any = Depends(get_current_user)):
    return current_user
