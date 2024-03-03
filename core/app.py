from fastapi import FastAPI

from app.account.api import app as account_router
from app.oauth2.api import app as oauth_router
app = FastAPI()
app.include_router(account_router)
app.include_router(oauth_router)


@app.get("/health")
async def check() -> dict:
    return {"status": "ok"}
