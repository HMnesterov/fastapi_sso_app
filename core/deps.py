from tortoise import Tortoise

from .app import app
from .settings import settings


@app.on_event("startup")
async def init_db():
    """Connect to db and launch migrations"""
    await Tortoise.init(db_url=settings.DB_URL,
                        modules={
                            "account": ["app.account.models"],
                            "client": ["app.client.models"]
                            # "migrate": ["core.migrate"]
                        })
    await Tortoise.generate_schemas()


@app.on_event("shutdown")
async def close_db_conn():
    """Close db connections"""
    await Tortoise.close_connections()
