import zipfile
from fastapi import HTTPException

def validate_zip(file_path: str):
    if not zipfile.is_zipfile(file_path):
        raise HTTPException(status_code=400, detail="Invalid ZIP file")

    with zipfile.ZipFile(file_path) as z:
        if not z.namelist():
            raise HTTPException(status_code=400, detail="Empty ZIP file")

        code_files = [
            f for f in z.namelist()
            if f.endswith((".py", ".js", ".java", ".ts"))
        ]

        if not code_files:
            raise HTTPException(status_code=400, detail="No source code found")
