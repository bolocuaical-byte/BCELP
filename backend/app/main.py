from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title="BCELP Backend",
    version=settings.APP_VERSION,
    description="BC Energy Lab Platform API",
)

app.include_router(router)
