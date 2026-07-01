from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.auth import Role, Permission


class RoleService:
    @staticmethod
    def create(db: Session, name: str, description: Optional[str] = None) -> Role:
        role = Role(name=name, description=description)
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    @staticmethod
    def get(db: Session, role_id: str) -> Optional[Role]:
        return db.query(Role).filter(Role.id == role_id, Role.is_deleted == False).one_or_none()

    @staticmethod
    def list(db: Session) -> List[Role]:
        return db.query(Role).filter(Role.is_deleted == False).all()

    @staticmethod
    def update(db: Session, role: Role, name: Optional[str] = None, description: Optional[str] = None) -> Role:
        if name is not None:
            role.name = name
        if description is not None:
            role.description = description
        db.commit()
        db.refresh(role)
        return role

    @staticmethod
    def delete(db: Session, role: Role) -> None:
        role.is_deleted = True
        db.commit()

    @staticmethod
    def assign_permission(db: Session, role: Role, permission: Permission) -> Role:
        if permission not in role.permissions:
            role.permissions.append(permission)
            db.commit()
            db.refresh(role)
        return role
