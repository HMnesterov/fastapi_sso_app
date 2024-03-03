import datetime
import os

from pytz import timezone

from core.settings import settings


def now() -> datetime.datetime:
    """Return current datetime"""
    return datetime.datetime.now(tz=timezone(settings.TZ))


def generate_random_string(length: int) -> str:
    return os.urandom(length).hex()[:length]
