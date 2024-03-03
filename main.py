import uvicorn

if __name__ == "__main__":
    uvicorn.run("core.deps:app", reload=True)
