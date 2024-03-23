import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="core.deps:app", host="0.0.0.0")
