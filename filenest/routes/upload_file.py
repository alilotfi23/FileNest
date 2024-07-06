# routes/upload_file.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import aiofiles
import os
import logging

router = APIRouter()

# BASE_DIR defaults to "file_storage" if it is not defined in the .env file
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
os.makedirs(BASE_DIR, exist_ok=True)


@router.post("/file/upload/{folder_name}/")
async def upload_file(folder_name: str, file: UploadFile = File(...)):
    folder_path = Path(BASE_DIR) / folder_name
    if not folder_path.exists():
        raise HTTPException(status_code=404, detail="Folder not found")

    file_location = folder_path / file.filename
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    logging.info(f"File '{file.filename}' uploaded to '{folder_name}'")
    return {"message": f"File '{file.filename}' saved at '{folder_name}'"}
