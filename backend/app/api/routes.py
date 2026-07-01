from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["system"])


@router.get("/", response_model=dict)
def read_root() -> dict:
    return {
        "project": "BCELP",
        "name": "BC Energy Lab Platform",
        "version": settings.app_version,
        "status": "running",
    }


@router.get("/health", response_model=dict)
def health_check() -> dict:
    return {"status": "ok"}
