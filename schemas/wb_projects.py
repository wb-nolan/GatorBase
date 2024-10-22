from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from models.wb_projects import DeletionProgress, ArchiveProgress, ActiveEnum
from typing import Optional
from pydantic import BaseModel, Field



class WbProjectBase(BaseModel):
    user_id: str
    fileset: int
    active: ActiveEnum #bool
    in_alfred: ActiveEnum #ool
    proj_name: Optional[str] = None #str
    studio: Optional[str] = None
    archivebarcode: Optional[str] = None
    lto: Optional[str] = None #str
    proj_path: Optional[str] = None #str
    proj_size: Optional[int] = None
    proj_size_gb: Optional[int] = None # Changed to Optional
    expected_end_date: Optional[datetime] = None
    deletion_progress: Optional[DeletionProgress] = None
    archive_progress: Optional[ArchiveProgress] = None
    date_added: Optional[datetime] = Field(default_factory=datetime.now)  # Set to current time by default
    date_modified: Optional[datetime] = Field(default_factory=datetime.now)  # Set to current time by default
    date_deleted: Optional[datetime] = Field(default=None)  # Nullable, defaults to None
    date_archived: Optional[datetime] = Field(default=None)
    notes: Optional[str] = None

class WbProjectCreate(WbProjectBase):
    date_added: datetime = Field(default_factory=datetime.now) 
    date_modified: datetime = Field(default_factory=datetime.now)

class WbProjectUpdate(WbProjectBase):
    user_id: Optional[str] = None
    fileset: Optional[int] = None
    active: ActiveEnum 
    in_alfred: ActiveEnum
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
    date_added: Optional[datetime] = Field(default_factory=datetime.now)  # Set to current time by default
    date_modified: Optional[datetime] = Field(default_factory=datetime.now)  # Set to current time by default
    date_deleted: Optional[datetime] = Field(default=None)  # Nullable, defaults to None
    date_archived: Optional[datetime] = Field(default=None) 
    notes: Optional[str] = None

class WbProjectResponse(WbProjectBase):
    id: int

    class Config:
        orm_mode = True
