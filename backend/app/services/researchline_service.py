from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.research import ResearchLine
from app.schemas.research import ResearchLineCreate, ResearchLineUpdate


class ResearchLineService:
    @staticmethod
    def create(db: Session, rl_in: ResearchLineCreate) -> ResearchLine:
        rl = ResearchLine(project_id=rl_in.project_id, title=rl_in.title, summary=rl_in.summary)
        db.add(rl)
        db.commit()
        db.refresh(rl)
        return rl

    @staticmethod
    def get(db: Session, rl_id: str) -> Optional[ResearchLine]:
        return db.query(ResearchLine).filter(ResearchLine.id == rl_id, ResearchLine.is_deleted == False).one_or_none()

    @staticmethod
    def list_by_project(db: Session, project_id: str) -> List[ResearchLine]:
        return db.query(ResearchLine).filter(ResearchLine.project_id == project_id, ResearchLine.is_deleted == False).all()

    @staticmethod
    def update(db: Session, rl: ResearchLine, rl_in: ResearchLineUpdate) -> ResearchLine:
        if rl_in.title is not None:
            rl.title = rl_in.title
        if rl_in.summary is not None:
            rl.summary = rl_in.summary
        db.commit()
        db.refresh(rl)
        return rl

    @staticmethod
    def delete(db: Session, rl: ResearchLine) -> None:
        rl.is_deleted = True
        db.commit()
