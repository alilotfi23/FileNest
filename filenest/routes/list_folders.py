# routes/list_folders.py

from fastapi import APIRouter
from pathlib import Path
import os
import logging

router = APIRouter()

# BASE_DIR defaults to "file_storage" if it is not defined in the .env file
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
os.makedirs(BASE_DIR, exist_ok=True)


@router.get("/folder/list")
async def list_folders():
    base_path = Path(BASE_DIR)
    folders = [d.name for d in base_path.iterdir() if d.is_dir()]
    logging.info("Folders listed")
    return {"folders": folders}
