from fastapi import FastAPI

from app.account.api import app as account_router

app = FastAPI()
app.include_router(account_router)


@app.get("/health")
async def check() -> dict:
    return {"status": "ok"}
