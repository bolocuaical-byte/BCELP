from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db_session, get_current_user
from app.schemas.core import ResearchGroupCreate, ResearchGroupRead
from app.services.researchgroup_service import ResearchGroupService

router = APIRouter(prefix="/research-groups", tags=["research-groups"])


@router.post("/", response_model=ResearchGroupRead, status_code=status.HTTP_201_CREATED)
def create_group(g_in: ResearchGroupCreate, db: Session = Depends(get_db_session), user=Depends(get_current_user)):
    return ResearchGroupService.create(db, g_in)


@router.get("/", response_model=List[ResearchGroupRead])
def list_groups(db: Session = Depends(get_db_session)):
    return ResearchGroupService.list(db)


@router.get("/{g_id}", response_model=ResearchGroupRead)
def get_group(g_id: str, db: Session = Depends(get_db_session)):
    g = ResearchGroupService.get(db, g_id)
    if not g:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Research group not found")
    return g


@router.put("/{g_id}", response_model=ResearchGroupRead)
def update_group(g_id: str, g_in: ResearchGroupCreate, db: Session = Depends(get_db_session)):
    g = ResearchGroupService.get(db, g_id)
    if not g:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Research group not found")
    return ResearchGroupService.update(db, g, name=g_in.name, description=g_in.description)


@router.delete("/{g_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_group(g_id: str, db: Session = Depends(get_db_session)):
    g = ResearchGroupService.get(db, g_id)
    if not g:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Research group not found")
    ResearchGroupService.delete(db, g)
    return None
