# backend/app/api/endpoints/jobs.py

from fastapi import APIRouter
from typing import List
import uuid

from app.schemas.job import Job, JobCreate

router = APIRouter()
jobs_db = {} # In-memory DB

@router.post("/", response_model=Job, status_code=201)
def create_job(job_in: JobCreate):
    job_id = str(uuid.uuid4())
    
    # Create a dictionary with all required fields
    job_data = job_in.dict()
    job_data['id'] = job_id
    
    # Store the Pydantic model in the DB for internal use
    db_job = Job(**job_data)
    jobs_db[job_id] = db_job
    
    # Return the dictionary, which FastAPI will validate against the response_model
    return job_data

@router.get("/", response_model=List[Job])
def read_jobs():
    # Convert the list of Pydantic models to a list of dictionaries for the response
    return [job.dict() for job in jobs_db.values()]