from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.lab import Equipment, Instrument, Sensor
from app.schemas.lab import EquipmentCreate


class EquipmentService:
    @staticmethod
    def create(db: Session, eq_in: EquipmentCreate) -> Equipment:
        eq = Equipment(
            name=eq_in.name,
            serial_number=eq_in.serial_number,
            model=eq_in.model,
            manufacturer=eq_in.manufacturer,
            location=eq_in.location,
            description=eq_in.description,
            laboratory_id=eq_in.laboratory_id,
        )
        db.add(eq)
        db.commit()
        db.refresh(eq)
        return eq

    @staticmethod
    def get(db: Session, eq_id: str) -> Optional[Equipment]:
        return db.query(Equipment).filter(Equipment.id == eq_id, Equipment.is_deleted == False).one_or_none()

    @staticmethod
    def list(db: Session) -> List[Equipment]:
        return db.query(Equipment).filter(Equipment.is_deleted == False).all()

    @staticmethod
    def update(db: Session, eq: Equipment, **fields) -> Equipment:
        for k, v in fields.items():
            if v is not None and hasattr(eq, k):
                setattr(eq, k, v)
        db.commit()
        db.refresh(eq)
        return eq

    @staticmethod
    def delete(db: Session, eq: Equipment):
        eq.is_deleted = True
        db.commit()
        return None

    @staticmethod
    def add_instrument(db: Session, equipment: Equipment, name: str, **kwargs) -> Instrument:
        inst = Instrument(equipment_id=equipment.id, name=name, **kwargs)
        db.add(inst)
        db.commit()
        db.refresh(inst)
        return inst

    @staticmethod
    def add_sensor(db: Session, instrument: Instrument, name: str, **kwargs) -> Sensor:
        s = Sensor(instrument_id=instrument.id, name=name, **kwargs)
        db.add(s)
        db.commit()
        db.refresh(s)
        return s
