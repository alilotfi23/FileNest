from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import StreamingResponse
from pathlib import Path
import aiofiles
import os
import logging

router = APIRouter()

# BASE_DIR defaults to "file_storage" if it is not defined in the .env file
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
BUFFER_SIZE = 1024 * 1024  # 1MB buffer size

# Ensure the base directory exists
os.makedirs(BASE_DIR, exist_ok=True)

# Dependency to construct file path
def get_file_path(folder_name: str, file_name: str) -> Path:
    return Path(BASE_DIR) / folder_name / file_name

@router.get("/file/download/{folder_name}/{file_name}")
async def download_file(file_path: Path = Depends(get_file_path)):
    if not file_path.exists():
        logging.error(f"File not found: {file_path}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    
    if not os.access(file_path, os.R_OK):
        logging.error(f"Access denied for file: {file_path}")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    try:
        async def iterfile():
            async with aiofiles.open(file_path, 'rb') as file:
                while chunk := await file.read(BUFFER_SIZE):
                    yield chunk

        logging.info(f"File downloaded: {file_path}")
        return StreamingResponse(iterfile(), media_type="application/octet-stream",
                                 headers={"Content-Disposition": f"attachment; filename={file_path.name}"})
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error reading file")

