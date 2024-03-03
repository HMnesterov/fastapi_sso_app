import datetime

from pytz import timezone

from core.settings import settings


def now() -> datetime.datetime:
    """Return current datetime"""
    return datetime.datetime.now(tz=timezone(settings.TZ))
