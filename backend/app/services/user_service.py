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
        return db.query(User).get(user_id)
