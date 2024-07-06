
## FileNest file manager Service

FileNest is simple API for managing folders and files in a file storage system using FastAPI.

## Features

- **Create Folders**: Endpoint to create folders in a specified directory.
- **Upload Files**: Endpoint to upload files to specific folders.
- **Download Files**: Endpoint to download files from specific folders.
- **List Files**: Endpoint to list files within specific folders.
- **List Folders**: Endpoint to list all folders in the storage directory.
- **Logging**: Logging setup to record folder and file operations.
- **Docker Support**: Docker configuration for easy deployment.

## Getting Started

### Prerequisites

- Python 3.7+
- Docker

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alilotfi23/FileNest.git
   cd FileNest
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
### Configuration

1. Create a `.env` file in the root directory of your project:

   ```dotenv
   BASE_DIR=file_storage
   ```

   Replace `"file_storage"` with the default directory name where you want to store folders and files.


### Usage

#### Running with Docker

To run the FastAPI application using Docker:

1. Build the Docker image:

   ```bash
   docker build -t fastapi-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 -v /host/path/to/file_storage:/app/file_storage fastapi-app
   ```

   Replace `/host/path/to/file_storage` with the actual path on your host machine where you want to store files.

3. Access the FastAPI application in your browser or using tools like `curl`:

   ```bash
   http://localhost:8000/docs
   ```

   This will open FastAPI's interactive documentation (Swagger UI) where you can test the endpoints.

#### API Endpoints

##### 1. Create Folder

- **POST /folder**: Endpoint to create a new folder. Provide the `folder_name` in the request body.

   Example using `curl`:

   ```bash
   curl -X 'POST' \
     'http://localhost:8000/folder' \
     -H 'Content-Type: application/json' \
     -d '{
       "folder_name": "new_folder"
     }'
   ```

##### 2. Upload File

- **POST /file/upload/{folder_name}**: Endpoint to upload a file to a specific folder. Replace `{folder_name}` with the name of the target folder.

   Example using `curl`:

   ```bash
   curl -X 'POST' \
     'http://localhost:8000/file/upload/new_folder' \
     -F 'file=@/path/to/local/file.txt'
   ```

##### 3. Download File

- **GET /file/download/{folder_name}/{file_name}**: Endpoint to download a file from a specific folder. Replace `{folder_name}` with the folder name and `{file_name}` with the file name.

   Example using `curl`:

   ```bash
   curl -OJL 'http://localhost:8000/file/download/new_folder/file.txt'
   ```

##### 4. List Files in Folder

- **GET /file/list/{folder_name}**: Endpoint to list files in a specific folder. Replace `{folder_name}` with the folder name.

   Example using `curl`:

   ```bash
   curl 'http://localhost:8000/file/list/new_folder'
   ```

##### 5. List All Folders

- **GET /folder/list**: Endpoint to list all folders in the storage directory.

   Example using `curl`:

   ```bash
   curl 'http://localhost:8000/folder/list'
   ```

## Logging

- Logs for folder and file operations are stored within the application. Ensure the appropriate permissions are set for the log files.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

