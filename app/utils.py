import datetime
import os

from pytz import timezone

from core.settings import settings


def now() -> datetime.datetime:
    """Return current datetime"""
    return datetime.datetime.now(tz=timezone(settings.TIMEZONE))


def generate_random_string(length: int) -> str:
    """Generate random string with defined length"""
    return os.urandom(length).hex()[:length]
