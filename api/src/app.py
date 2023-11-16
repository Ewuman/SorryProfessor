from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def on_startup() -> None:
    """Initialize database when starting API server."""
    pass

@app.on_event("shutdown")
def on_shutdown() -> None:
    pass

@app.get("/test")
def get_test():
    print("hi")