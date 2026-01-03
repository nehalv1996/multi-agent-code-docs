from fastapi import FastAPI
from .database import Base, engine
from .auth import router as auth_router
from .projects import router as project_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Multi-Agent Code Analysis & Documentation System",
    version="1.0"
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(project_router, prefix="/projects", tags=["Projects"])

@app.get("/")
def root():
    return {"message": "Backend is running"}
