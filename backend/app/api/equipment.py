from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db_session, get_current_user
from app.schemas.lab import EquipmentCreate, EquipmentRead, EquipmentUpdate
from app.services.equipment_service import EquipmentService

router = APIRouter(prefix="/equipment", tags=["equipment"])


@router.post("/", response_model=EquipmentRead, status_code=status.HTTP_201_CREATED)
def create_equipment(eq_in: EquipmentCreate, db: Session = Depends(get_db_session), user=Depends(get_current_user)):
    eq = EquipmentService.create(db, eq_in)
    return EquipmentRead.from_orm(eq)


@router.get("/", response_model=List[EquipmentRead])
def list_equipment(db: Session = Depends(get_db_session)):
    eqs = EquipmentService.list(db)
    return [EquipmentRead.from_orm(e) for e in eqs]


@router.get("/{eq_id}", response_model=EquipmentRead)
def get_equipment(eq_id: str, db: Session = Depends(get_db_session)):
    eq = EquipmentService.get(db, eq_id)
    if not eq:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
    return EquipmentRead.from_orm(eq)


@router.put("/{eq_id}", response_model=EquipmentRead)
def update_equipment(eq_id: str, eq_in: EquipmentUpdate, db: Session = Depends(get_db_session)):
    eq = EquipmentService.get(db, eq_id)
    if not eq:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
    updated = EquipmentService.update(db, eq, **eq_in.model_dump(exclude_unset=True))
    return EquipmentRead.from_orm(updated)


@router.delete("/{eq_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equipment(eq_id: str, db: Session = Depends(get_db_session)):
    eq = EquipmentService.get(db, eq_id)
    if not eq:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
    EquipmentService.delete(db, eq)
    return None
