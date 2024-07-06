# routes/create_folder.py

from fastapi import APIRouter, HTTPException
from pathlib import Path
import os
import logging

router = APIRouter()

# BASE_DIR defaults to "file_storage" if it is not defined in the .env file
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
os.makedirs(BASE_DIR, exist_ok=True)


@router.post("/folder")
async def create_folder(folder_name: str):
    folder_path = Path(BASE_DIR) / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)
    logging.info(f"Folder '{folder_name}' created successfully")
    return {"message": f"Folder '{folder_name}' created successfully"}
