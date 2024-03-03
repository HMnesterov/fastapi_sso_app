from typing import Optional

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    DB_URL: str
    SESSION_LIFE: int
    TZ: str
    #PASSWORD_HASHER: str
    #SALT: bytes
    # DB_MIGRATE_PATH: str
    class Config:
        env_file = "env/.env"
        env_file_encoding = "utf-8"


settings = AppSettings()
