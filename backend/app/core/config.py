from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")


class Settings(BaseSettings):
    app_name: str = Field("BCELP Backend", env="APP_NAME")
    app_version: str = Field("0.1.0", env="APP_VERSION")
    environment: str = Field("development", env="ENVIRONMENT")

    postgres_user: str = Field("bcelp_user", env="POSTGRES_USER")
    postgres_password: str = Field("bcelp_password", env="POSTGRES_PASSWORD")
    postgres_db: str = Field("bcelp_db", env="POSTGRES_DB")
    postgres_host: str = Field("postgres", env="POSTGRES_HOST")
    postgres_port: int = Field(5432, env="POSTGRES_PORT")
    database_url: str = Field(
        "postgresql+psycopg2://bcelp_user:bcelp_password@postgres:5432/bcelp_db",
        env="DATABASE_URL",
    )

    jwt_secret_key: str = Field("your-secret-key", env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")
    jwt_access_token_expires_minutes: int = Field(60, env="JWT_ACCESS_TOKEN_EXPIRE_MINUTES")

    cors_origins: List[str] = Field(["*"], env="CORS_ORIGINS")

    class Config:
        env_file = Path(__file__).resolve().parents[2] / ".env"
        env_file_encoding = "utf-8"


settings = Settings()
