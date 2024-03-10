from typing import Optional

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    DB_URL: str
    # DB_MIGRATE_PATH: str

    SESSION_LIFE: int
    TIMEZONE: str

    # jwt
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = "env/.env"
        env_file_encoding = "utf-8"


settings = AppSettings()
