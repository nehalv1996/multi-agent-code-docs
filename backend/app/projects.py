from fastapi import APIRouter, UploadFile, File, Form
import os
import uuid
from .utils import validate_zip
from .database import SessionLocal
from .models import Project

router = APIRouter()

@router.post("/create")
async def create_project(
    name: str = Form(...),
    personas: str = Form(...),
    zipfile: UploadFile = File(None)
):
    project_id = str(uuid.uuid4())

    if zipfile:
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{project_id}.zip"
        with open(file_path, "wb") as f:
            f.write(await zipfile.read())
        validate_zip(file_path)

    db = SessionLocal()
    project = Project(
        id=project_id,
        owner_email="demo_user",
        name=name,
        personas=personas,
        status="ANALYSIS_STARTED"
    )
    db.add(project)
    db.commit()

    return {
        "project_id": project_id,
        "status": "ANALYSIS_STARTED"
    }
