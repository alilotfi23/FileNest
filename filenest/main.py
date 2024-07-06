# main.py

from fastapi import FastAPI
from routes.create_folder import router as create_folder_router
from routes.upload_file import router as upload_file_router
from routes.download_file import router as download_file_router
from routes.list_files import router as list_files_router
from routes.list_folders import router as list_folders_router

app = FastAPI()

app.include_router(create_folder_router)
app.include_router(upload_file_router)
app.include_router(download_file_router)
app.include_router(list_files_router)
app.include_router(list_folders_router)

