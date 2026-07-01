from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.research import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:
    @staticmethod
    def create(db: Session, owner_id: str, project_in: ProjectCreate) -> Project:
        project = Project(name=project_in.name, description=project_in.description, owner_id=owner_id, status=project_in.status)
        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    @staticmethod
    def get(db: Session, project_id: str) -> Optional[Project]:
        return db.query(Project).filter(Project.id == project_id, Project.is_deleted == False).one_or_none()

    @staticmethod
    def list(db: Session) -> List[Project]:
        return db.query(Project).filter(Project.is_deleted == False).all()

    @staticmethod
    def update(db: Session, project: Project, project_in: ProjectUpdate) -> Project:
        if project_in.name is not None:
            project.name = project_in.name
        if project_in.description is not None:
            project.description = project_in.description
        if project_in.status is not None:
            project.status = project_in.status
        db.commit()
        db.refresh(project)
        return project

    @staticmethod
    def delete(db: Session, project: Project) -> None:
        project.is_deleted = True
        db.commit()
