from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.auth import Permission


class PermissionService:
    @staticmethod
    def create(db: Session, name: str, description: Optional[str] = None) -> Permission:
        permission = Permission(name=name, description=description)
        db.add(permission)
        db.commit()
        db.refresh(permission)
        return permission

    @staticmethod
    def get(db: Session, permission_id: str) -> Optional[Permission]:
        return db.query(Permission).filter(Permission.id == permission_id, Permission.is_deleted == False).one_or_none()

    @staticmethod
    def list(db: Session) -> List[Permission]:
        return db.query(Permission).filter(Permission.is_deleted == False).all()

    @staticmethod
    def update(db: Session, permission: Permission, name: Optional[str] = None, description: Optional[str] = None) -> Permission:
        if name is not None:
            permission.name = name
        if description is not None:
            permission.description = description
        db.commit()
        db.refresh(permission)
        return permission

    @staticmethod
    def delete(db: Session, permission: Permission) -> None:
        permission.is_deleted = True
        db.commit()
