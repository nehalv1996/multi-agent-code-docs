import zipfile
import os
import re
import subprocess
import tempfile
import shutil
from fastapi import HTTPException

CODE_EXTENSIONS = (
    ".py", ".js", ".ts", ".java", ".go", ".cpp", ".c", ".cs", ".rb", ".php"
)

def validate_zip(file_path: str):

    if not zipfile.is_zipfile(file_path):
        raise ValueError(
            "Invalid or corrupted ZIP file. Please upload a valid ZIP archive."
        )

    try:
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            file_list = zip_ref.namelist()

    except Exception:
        raise ValueError(
            "Unable to read ZIP file. The file may be corrupted"
        )
    
    if not file_list:
        raise ValueError(
            "The uploaded ZIP file is empty. Please upload a repository with source code."
        )
    
    code_files_found = False

    for file_name in file_list:
        _, ext = os.path.splitext(file_name.lower())
        if ext in CODE_EXTENSIONS:
            code_files_found = True
            break

    if not code_files_found:
        raise ValueError(
            "No recognizable source code found in the ZIP file. "
            "Please upload a valid code repository."
        )    
    

def clone_github_repo(github_url: str) -> str:
    if not re.match(r"^https://github.com/[^/]+[^/]+$", github_url):
        raise ValueError(
            "Invalid GitHub URL. Expected format: https://github.com/owner/repository"
        )
    
    temp_dir = tempfile.mkdtemp(prefix="repo_")

    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", github_url, temp_dir],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, 
        )
    except Exception:
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise ValueError(
            "Unable to access the Github repository. "
            "It may be private, unavailable, or the URL is incorrect."
        )
    
    return temp_dir