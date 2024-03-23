import sys
import logging

LOG_FMT = "%(asctime)s - [%(levelname)s] -  %(name)s - %(funcName)s(%(lineno)d) - %(message)s"
LOG_DATE_FMT = "%Y-%m-%d %H:%M:%S"

fmt = logging.Formatter(fmt=LOG_FMT, datefmt=LOG_DATE_FMT)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(fmt)

# Application
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(sh)

# Uvicorn
logger_uvicorn = logging.getLogger("uvicorn")
logger_uvicorn.setLevel(logging.DEBUG)
logger_uvicorn.propagate = False
logger_uvicorn.addHandler(sh)

# Tortoise
logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(sh)
