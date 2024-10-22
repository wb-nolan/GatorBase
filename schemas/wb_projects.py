from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from models.wb_projects import DeletionProgress, ArchiveProgress
from typing import Optional


class WbProjectBase(BaseModel):
    user_id: str
    fileset: int
    active: bool
    in_alfred: bool
    proj_name: str
    studio: Optional[str] = None
    archivebarcode: Optional[str] = None
    lto: str
    proj_path: str
    proj_size: Optional[int] = None
    proj_size_gb: Optional[int] = None # Changed to Optional
    expected_end_date: Optional[datetime] = None
    deletion_progress: Optional[DeletionProgress] = None
    archive_progress: Optional[ArchiveProgress] = None
    date_added: datetime = Optional[datetime] = None 
    date_modified: datetime = Optional[datetime] = None
    date_deleted: Optional[datetime] = None
    date_archived: Optional[datetime] = None
    notes: Optional[str] = None

class WbProjectCreate(WbProjectBase):
    date_added: datetime = Field(default_factory=datetime.now) 
    date_modified: datetime = Field(default_factory=datetime.now)

class WbProjectUpdate(WbProjectBase):
    user_id: Optional[str] = None
    fileset: Optional[int] = None
    active: Optional[bool] = None
    in_alfred: Optional[bool] = None
    proj_name: Optional[str] = None
    studio: Optional[str] = None
    archivebarcode: Optional[str] = None
    lto: Optional[str] = None
    proj_path: Optional[str] = None
    proj_size: Optional[int] = None
    proj_size_gb: Optional[int] = None
    expected_end_date: Optional[datetime] = None
    deletion_progress: Optional[DeletionProgress] = None
    archive_progress: Optional[ArchiveProgress] = None
    date_modified: datetime = Field(default_factory=datetime.now)
    date_deleted: Optional[datetime] = None
    date_archived: Optional[datetime] = None
    notes: Optional[str] = None

class WbProjectResponse(WbProjectBase):
    id: int

    class Config:
        orm_mode = True
