from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db_session, get_current_user
from app.schemas.research import ResearchLineCreate, ResearchLineRead, ResearchLineUpdate
from app.services.researchline_service import ResearchLineService

router = APIRouter(prefix="/research-lines", tags=["research-lines"])


@router.post("/", response_model=ResearchLineRead, status_code=status.HTTP_201_CREATED)
def create_research_line(rl_in: ResearchLineCreate, db: Session = Depends(get_db_session), user=Depends(get_current_user)):
    return ResearchLineService.create(db, rl_in)


@router.get("/{rl_id}", response_model=ResearchLineRead)
def get_research_line(rl_id: str, db: Session = Depends(get_db_session)):
    rl = ResearchLineService.get(db, rl_id)
    if not rl:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Research line not found")
    return rl


@router.put("/{rl_id}", response_model=ResearchLineRead)
def update_research_line(rl_id: str, rl_in: ResearchLineUpdate, db: Session = Depends(get_db_session)):
    rl = ResearchLineService.get(db, rl_id)
    if not rl:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Research line not found")
    return ResearchLineService.update(db, rl, rl_in)


@router.delete("/{rl_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_research_line(rl_id: str, db: Session = Depends(get_db_session)):
    rl = ResearchLineService.get(db, rl_id)
    if not rl:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Research line not found")
    ResearchLineService.delete(db, rl)
    return None
