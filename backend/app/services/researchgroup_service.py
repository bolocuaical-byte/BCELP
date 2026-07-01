from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.core_domain import ResearchGroup
from app.schemas.core import ResearchGroupCreate, ResearchGroupRead


class ResearchGroupService:
    @staticmethod
    def create(db: Session, rg_in: ResearchGroupCreate) -> ResearchGroup:
        rg = ResearchGroup(name=rg_in.name, description=rg_in.description)
        db.add(rg)
        db.commit()
        db.refresh(rg)
        return rg

    @staticmethod
    def get(db: Session, rg_id: str) -> Optional[ResearchGroup]:
        return db.query(ResearchGroup).filter(ResearchGroup.id == rg_id, ResearchGroup.is_deleted == False).one_or_none()

    @staticmethod
    def list(db: Session) -> List[ResearchGroup]:
        return db.query(ResearchGroup).filter(ResearchGroup.is_deleted == False).all()

    @staticmethod
    def update(db: Session, rg: ResearchGroup, name: Optional[str] = None, description: Optional[str] = None) -> ResearchGroup:
        if name is not None:
            rg.name = name
        if description is not None:
            rg.description = description
        db.commit()
        db.refresh(rg)
        return rg

    @staticmethod
    def delete(db: Session, rg: ResearchGroup) -> None:
        rg.is_deleted = True
        db.commit()
