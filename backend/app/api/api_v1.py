from fastapi import APIRouter
from app.api.endpoints import jobs, cvs

api_router = APIRouter()
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(cvs.router, prefix="/cvs", tags=["cvs"])