from typing import Optional

from sqlalchemy.orm import Session

from app.models.auth import User
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService


class UserService:
    @staticmethod
    def create(db: Session, user_in: UserCreate) -> User:
        hashed = AuthService.get_password_hash(user_in.password)
        user = User(email=user_in.email, hashed_password=hashed, full_name=user_in.full_name)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email, User.is_deleted == False).one_or_none()

    @staticmethod
    def get(db: Session, user_id: str) -> Optional[User]:
        return db.query(User).filter(User.id == user_id, User.is_deleted == False).one_or_none()

    @staticmethod
    def list(
        db: Session,
        skip: int = 0,
        limit: int = 20,
        email: Optional[str] = None,
        full_name: Optional[str] = None,
        is_active: Optional[bool] = None,
    ) -> list[User]:
        query = db.query(User).filter(User.is_deleted == False)
        if email is not None:
            query = query.filter(User.email.ilike(f"%{email}%"))
        if full_name is not None:
            query = query.filter(User.full_name.ilike(f"%{full_name}%"))
        if is_active is not None:
            query = query.filter(User.is_active == is_active)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, user: User, user_in: UserUpdate) -> User:
        if user_in.email is not None:
            user.email = user_in.email
        if user_in.full_name is not None:
            user.full_name = user_in.full_name
        if user_in.is_active is not None:
            user.is_active = user_in.is_active
        if user_in.password is not None:
            user.hashed_password = AuthService.get_password_hash(user_in.password)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete(db: Session, user: User) -> None:
        user.is_deleted = True
        db.commit()
