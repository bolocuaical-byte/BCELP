from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db_session, get_current_user
from app.models.lab import Equipment, MaintenanceEvent
from app.schemas.lab import LabCreate, LabRead, LabUpdate
from app.models.lab import Equipment

router = APIRouter(prefix="/labs", tags=["labs"])


@router.get("/", response_model=List[LabRead])
def list_labs(db: Session = Depends(get_db_session)):
    # Laboratories are represented via Equipment locations; return distinct locations as simple labs
    equipments = db.query(Equipment).filter(Equipment.is_deleted == False).all()
    labs = []
    for e in equipments:
        labs.append(LabRead(id=str(e.id), name=e.name, location=e.location, description=e.description))
    return labs


@router.post("/", response_model=LabRead, status_code=status.HTTP_201_CREATED)
def create_lab(lab_in: LabCreate, db: Session = Depends(get_db_session), user=Depends(get_current_user)):
    # Simple lab creation represented as an Equipment with no serial
    eq = Equipment(name=lab_in.name, serial_number=None, location=lab_in.location, description=lab_in.description)
    db.add(eq)
    db.commit()
    db.refresh(eq)
    return LabRead(id=str(eq.id), name=eq.name, location=eq.location, description=eq.description)


@router.get("/{lab_id}", response_model=LabRead)
def get_lab(lab_id: str, db: Session = Depends(get_db_session)):
    eq = db.query(Equipment).filter(Equipment.id == lab_id, Equipment.is_deleted == False).one_or_none()
    if not eq:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lab not found")
    return LabRead(id=str(eq.id), name=eq.name, location=eq.location, description=eq.description)


@router.put("/{lab_id}", response_model=LabRead)
def update_lab(lab_id: str, lab_in: LabUpdate, db: Session = Depends(get_db_session)):
    eq = db.query(Equipment).filter(Equipment.id == lab_id, Equipment.is_deleted == False).one_or_none()
    if not eq:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lab not found")
    if lab_in.name is not None:
        eq.name = lab_in.name
    if lab_in.location is not None:
        eq.location = lab_in.location
    if lab_in.description is not None:
        eq.description = lab_in.description
    db.commit()
    db.refresh(eq)
    return LabRead(id=str(eq.id), name=eq.name, location=eq.location, description=eq.description)


@router.delete("/{lab_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab(lab_id: str, db: Session = Depends(get_db_session)):
    eq = db.query(Equipment).filter(Equipment.id == lab_id, Equipment.is_deleted == False).one_or_none()
    if not eq:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lab not found")
    eq.is_deleted = True
    db.commit()
    return None
