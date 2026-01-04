from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import os
import uuid
import shutil

from .utils import validate_zip, clone_github_repo
from .database import SessionLocal
from .models import Project

router = APIRouter()

# =====================================
# CONFIGURATION
# =====================================

MAX_ZIP_SIZE = 100 * 1024 * 1024   # 100 MB

@router.post("/create")
async def create_project(
    name: str = Form(...),
    personas: str = Form(...),
    zipfile: UploadFile = File(None),
    github_url: str = Form(None),
):

    if not zipfile and not github_url:
        raise HTTPException(
            status_code=400,
            detail="Please upload a ZIP file or provide a Github repository URL"
        )

    project_id = str(uuid.uuid4())
    working_path = None

    if zipfile:
        if zipfile.size is not None and zipfile.size > MAX_ZIP_SIZE:
            raise HTTPException(
                status_code=400,
                detail="Uploaded ZIP file is too large. Maximum allowed size is 100 MB."
            )
    
    
    
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{project_id}.zip"
        with open(file_path, "wb") as f:
            f.write(await zipfile.read())
        try:
            validate_zip(file_path)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        working_path = file_path

    if github_url:
        try:
            repo_path = clone_github_repo(github_url)
            working_path = repo_path
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))


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
    db.close()

    return {
        "project_id": project_id,
        "status": "ANALYSIS_STARTED",
        "message": "Project created successfully. Analysis started."
    }
