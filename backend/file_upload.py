
from fastapi import APIRouter, File, UploadFile, HTTPException
import os

UPLOAD_FOLDER = "./uploads/"
MAX_FILE_SIZE = 1.5 * 1024 * 1024  # 1.5 MB

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "File uploaded successfully", "filename": file.filename}
        