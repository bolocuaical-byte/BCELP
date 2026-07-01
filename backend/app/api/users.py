from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db_session
from app.models.auth import Role, Permission, User
from app.schemas.user import (
    PermissionCreate,
    PermissionRead,
    PermissionUpdate,
    RoleCreate,
    RoleRead,
    RoleUpdate,
    UserCreate,
    UserRead,
    UserUpdate,
)
from app.services.permission_service import PermissionService
from app.services.role_service import RoleService
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserRead])
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    email: Optional[str] = Query(None),
    username: Optional[str] = Query(None),
    is_active: Optional[bool] = Query(None),
    db: Session = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
):
    users = UserService.list(db, skip=skip, limit=limit, email=email, full_name=username, is_active=is_active)
    return users


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    return UserService.create(db, user_in)


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: str, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    user = UserService.get(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: str, user_in: UserUpdate, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    user = UserService.get(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserService.update(db, user, user_in)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    user = UserService.get(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    UserService.delete(db, user)
    return None


router_roles = APIRouter(prefix="/roles", tags=["roles"])


@router_roles.get("/", response_model=List[RoleRead])
def list_roles(db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    return RoleService.list(db)


@router_roles.post("/", response_model=RoleRead, status_code=status.HTTP_201_CREATED)
def create_role(role_in: RoleCreate, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    return RoleService.create(db, role_in.name, role_in.description)


@router_roles.get("/{role_id}", response_model=RoleRead)
def get_role(role_id: str, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    role = RoleService.get(db, role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return role


@router_roles.put("/{role_id}", response_model=RoleRead)
def update_role(role_id: str, role_in: RoleUpdate, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    role = RoleService.get(db, role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return RoleService.update(db, role, role_in.name, role_in.description)


@router_roles.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: str, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    role = RoleService.get(db, role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    RoleService.delete(db, role)
    return None


router_permissions = APIRouter(prefix="/permissions", tags=["permissions"])


@router_permissions.get("/", response_model=List[PermissionRead])
def list_permissions(db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    return PermissionService.list(db)


@router_permissions.post("/", response_model=PermissionRead, status_code=status.HTTP_201_CREATED)
def create_permission(permission_in: PermissionCreate, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    return PermissionService.create(db, permission_in.name, permission_in.description)


@router_permissions.get("/{permission_id}", response_model=PermissionRead)
def get_permission(permission_id: str, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    permission = PermissionService.get(db, permission_id)
    if not permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found")
    return permission


@router_permissions.put("/{permission_id}", response_model=PermissionRead)
def update_permission(permission_id: str, permission_in: PermissionUpdate, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    permission = PermissionService.get(db, permission_id)
    if not permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found")
    return PermissionService.update(db, permission, permission_in.name, permission_in.description)


@router_permissions.delete("/{permission_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_permission(permission_id: str, db: Session = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    permission = PermissionService.get(db, permission_id)
    if not permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found")
    PermissionService.delete(db, permission)
    return None
