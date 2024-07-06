# routes/download_file.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pathlib import Path
import aiofiles
import os
import logging

router = APIRouter()

# BASE_DIR defaults to "file_storage" if it is not defined in the .env file
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
os.makedirs(BASE_DIR, exist_ok=True)


@router.get("/file/download/{folder_name}/{file_name}")
async def download_file(folder_name: str, file_name: str):
    file_path = Path(BASE_DIR) / folder_name / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    async def iterfile():
        async with aiofiles.open(file_path, 'rb') as f:
            while chunk := await f.read(1024 * 1024):
                yield chunk

    logging.info(f"File '{file_name}' downloaded from '{folder_name}'")
    return StreamingResponse(iterfile(), media_type="application/octet-stream",
                             headers={"Content-Disposition": f"attachment; filename={file_name}"})
