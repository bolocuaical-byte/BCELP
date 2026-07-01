from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

ACCESS_TOKEN_EXPIRE_MINUTES = settings.jwt_access_token_expires_minutes
ALGORITHM = settings.jwt_algorithm
SECRET_KEY = settings.jwt_secret_key
