# routes/upload_file.py

from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pathlib import Path
import aiofiles
import os
import logging

router = APIRouter()

# BASE_DIR defaults to "file_storage" if it is not defined in the .env file
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
os.makedirs(BASE_DIR, exist_ok=True)


@router.post("/file/upload/{folder_name}/", status_code=status.HTTP_201_CREATED)
async def upload_file(folder_name: str, file: UploadFile = File(...)):
    base_dir = Path(os.getenv("BASE_DIR", "file_storage"))
    folder_path = base_dir / folder_name
    if not folder_path.exists():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Folder not found")

    file_location = folder_path / file.filename
    if file_location.exists():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="File already exists")

    async with aiofiles.open(file_location, 'wb') as out_file:
        while content := await file.read(8192):  # Adjusted chunk size for potentially better performance
            await out_file.write(content)

    logging.info(f"File '{file.filename}' uploaded to '{folder_name}'")
    return {"message": f"File '{file.filename}' saved at '{folder_name}'"}
