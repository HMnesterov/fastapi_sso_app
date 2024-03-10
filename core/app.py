from fastapi import FastAPI

from app.account.api import router as account_router
from app.client.api import router as client_router
from app.oidc.api import router as oidc_router

app = FastAPI()
app.include_router(account_router)
app.include_router(client_router)
app.include_router(oidc_router)


@app.get("/health")
async def check() -> dict:
    return {"status": "ok"}
