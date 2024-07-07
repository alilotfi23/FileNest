from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from pathlib import Path
import os
import logging

router = APIRouter()

# Assuming logging is configured in the main application configuration
logger = logging.getLogger(__name__)

# Base directory should ideally be set in your application's startup event
BASE_DIR = os.getenv("BASE_DIR", "file_storage")
Path(BASE_DIR).mkdir(exist_ok=True)

class FolderResponse(BaseModel):
    message: str

@router.post("/folder", response_model=FolderResponse)
async def create_folder(folder_name: str):
    try:
        folder_path = Path(BASE_DIR) / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Folder '{folder_name}' created successfully")
        return FolderResponse(message=f"Folder '{folder_name}' created successfully")
    except Exception as e:
        logger.error(f"Error creating folder '{folder_name}': {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An error occurred while creating the folder.")

