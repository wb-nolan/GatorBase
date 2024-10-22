from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from models.md5_verify_queue import TaskTypeStatus, Status
from typing import Optional

class md5VerifyQueueBase(BaseModel):
    user_id: Optional[str] = None
    hostname: Optional[str] = None
    char_scan: Status 
    log: Optional[str] = None
    task_type: Optional[TaskTypeStatus] = None
    status: Status
    verify_status: Status
    compare_status: Status
    progress: Optional[str] = None
    eta: Optional[str] = None
    proj_name: str # FK - wb_projects
    md5_path: Optional[str] = None
    md5_name: Optional[str] = None
    md5_size: Optional[str] = None
    src_count: Optional[int] = None
    md5_count: Optional[int] = None
    verify_md5_count: Optional[int] = None
    compare_md5_count: Optional[int] = None
    verify_md5_name: Optional[str] = None
    verify_md5_path: Optional[str] = None
    compare_md5_path: Optional[str] = None
    compare_md5_name: Optional[str] = None
    src_name: Optional[str] = None
    src_path: Optional[str] = None
    src_size: Optional[str] = None
    date_added: Optional[datetime] = None 
    date_started: Optional[datetime] = None  
    date_completed: Optional[datetime] = None 
    date_modified: Optional[datetime] = None

class md5VerifyQueueCreate(md5VerifyQueueBase):
    date_added: datetime = Field(default_factory=datetime.now) 
    date_started: datetime = Field(default_factory=datetime.now)
    date_modified: datetime = Field(default_factory=datetime.now)

class md5VerifyQueueUpdate(md5VerifyQueueBase):
    user_id: Optional[str] = None
    hostname: Optional[str] = None
    char_scan: Status 
    log: Optional[str] = None
    task_type: Optional[TaskTypeStatus] = None
    status: Status
    verify_status: Status
    compare_status: Status
    progress: Optional[str] = None
    eta: Optional[str] = None
    proj_name: str # FK - wb_projects
    md5_path: Optional[str] = None
    md5_name: Optional[str] = None
    md5_size: Optional[str] = None
    src_count: Optional[int] = None
    md5_count: Optional[int] = None
    verify_md5_count: Optional[int] = None
    compare_md5_count: Optional[int] = None
    verify_md5_name: Optional[str] = None
    verify_md5_path: Optional[str] = None
    compare_md5_path: Optional[str] = None
    compare_md5_name: Optional[str] = None
    src_name: Optional[str] = None
    src_path: Optional[str] = None
    src_size: Optional[str] = None
    # update when Status moves from PENDING to IN_PROGESS
    date_started: Optional[datetime] = None
    date_completed: Optional[datetime] = None
    date_modified: datetime = Field(default_factory=datetime.now) 

class md5VerifyQueueResponse(md5VerifyQueueBase):
    id: int

    class Config:
        orm_mode = True