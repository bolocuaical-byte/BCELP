from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.lab import Laboratory
from app.schemas.lab import LabCreate


class LaboratoryService:
    @staticmethod
    def create(db: Session, lab_in: LabCreate) -> Laboratory:
        lab = Laboratory(name=lab_in.name, location=lab_in.location, description=lab_in.description)
        db.add(lab)
        db.commit()
        db.refresh(lab)
        return lab

    @staticmethod
    def get(db: Session, lab_id: str) -> Optional[Laboratory]:
        return db.query(Laboratory).filter(Laboratory.id == lab_id, Laboratory.is_deleted == False).one_or_none()

    @staticmethod
    def list(db: Session) -> List[Laboratory]:
        return db.query(Laboratory).filter(Laboratory.is_deleted == False).all()

    @staticmethod
    def update(db: Session, lab: Laboratory, **fields) -> Laboratory:
        for k, v in fields.items():
            if v is not None and hasattr(lab, k):
                setattr(lab, k, v)
        db.commit()
        db.refresh(lab)
        return lab

    @staticmethod
    def delete(db: Session, lab: Laboratory):
        lab.is_deleted = True
        db.commit()
        return None
