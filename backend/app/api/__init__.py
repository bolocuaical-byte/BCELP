from fastapi import APIRouter

from app.api.routes import router as routes_router
from app.api.auth import router as auth_router
from app.api.users import router as users_router, router_roles, router_permissions
from app.api.projects import router as projects_router
from app.api.labs import router as labs_router
from app.api.research_lines import router as research_lines_router
from app.api.research_groups import router as research_groups_router
from app.api.equipment import router as equipment_router

api_router = APIRouter()
api_router.include_router(routes_router)
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(router_roles)
api_router.include_router(router_permissions)
api_router.include_router(projects_router)
api_router.include_router(labs_router)
api_router.include_router(research_lines_router)
api_router.include_router(research_groups_router)
api_router.include_router(equipment_router)
