# routes/list_files.py

from fastapi import APIRouter, HTTPException
from pathlib import Path
import os
import logging

router = APIRouter()

# BASE_DIR defaults to "file_storage" if it is not defined in the .env file
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
os.makedirs(BASE_DIR, exist_ok=True)


@router.get("/file/list/{folder_name}")
async def list_files(folder_name: str):
    folder_path = Path(BASE_DIR) / folder_name
    if not folder_path.exists():
        raise HTTPException(status_code=404, detail="Folder not found")

    files = [{"name": f, "size": os.path.getsize(os.path.join(folder_path, f))} for f in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, f))]
    logging.info(f"Files listed in folder '{folder_name}'")
    return {"files": files}
