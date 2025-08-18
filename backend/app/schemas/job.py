# backend/app/schemas/job.py

from pydantic import BaseModel, ConfigDict 
from typing import List

class JobBase(BaseModel):
    title: str
    description: str
    requirements: List[str]

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: str
    
    
    model_config = ConfigDict(from_attributes=True)