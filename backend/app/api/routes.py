from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=dict)
def read_root():
    return {
        "project": "BCELP",
        "name": "BC Energy Lab Platform",
        "version": settings.APP_VERSION,
        "status": "running",
    }


@router.get("/health", response_model=dict)
def health_check():
    return {"status": "ok"}
