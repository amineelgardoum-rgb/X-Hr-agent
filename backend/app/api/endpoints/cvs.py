from fastapi import APIRouter, UploadFile, File
from app.services import cv_pareser
router = APIRouter()
cvs_db = {} # In-memory DB

@router.post("/upload/", status_code=201)
async def upload_cv(file: UploadFile = File(...)):
    parsed_data = cv_pareser.parse_cv_file(file.filename)
    cvs_db[file.filename] = parsed_data
    return {"filename": file.filename, "parsed_skills": parsed_data["skills"]}