from typing import Optional

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Application settings class"""
    DB_URL: str
    # DB_MIGRATE_PATH: str

    SESSION_LIFE: int
    TIMEZONE: str

    # jwt
    SECRET_KEY: str
    ALGORITHM: str
    SESSION_COOKIE_NAME: Optional[str] = "session_key"

    class Config:
        env_file = "env/.env"
        env_file_encoding = "utf-8"


settings = AppSettings()
