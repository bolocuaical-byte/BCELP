from fastapi import APIRouter

from app.api.routes import router as routes_router
from app.api.auth import router as auth_router
from app.api.users import router as users_router, router_roles, router_permissions

api_router = APIRouter()
api_router.include_router(routes_router)
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(router_roles)
api_router.include_router(router_permissions)
