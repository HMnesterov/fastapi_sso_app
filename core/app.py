from fastapi import FastAPI

from app.account.api import app as account_router
from app.client.api import app as client_router
app = FastAPI()
app.include_router(account_router)
app.include_router(client_router)


@app.get("/health")
async def check() -> dict:
    return {"status": "ok"}
