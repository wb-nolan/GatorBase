from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from enum import Enum as PyEnum
from datetime import datetime
from pydantic import BaseModel, Field

class ActiveEnum(str, PyEnum):
    YES = 'YES'
    NO = 'NO'


class DeletionProgress(str, PyEnum):
    PENDING = 'PENDING'
    READY = 'READY'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

class ArchiveProgress(str, PyEnum):
    PENDING = 'PENDING'
    READY_FOR_ARCHIVE = 'READY_FOR_ARCHIVE'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

class WbProjects(Base):
    __tablename__ = 'wb_projects'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(11))
    fileset = Column(Integer)
    active = Column(Enum(ActiveEnum)) ### CHANGED
    in_alfred = Column(Enum(ActiveEnum)) ### CHANGED
    proj_name = Column(String(50), unique=True) # ADDED Unique
    studio = Column(String(255))
    archivebarcode = Column(String(11))
    lto = Column(String(11)) 
    proj_path = Column(String(255))
    proj_size = Column(Integer)
    proj_size_gb = Column(Integer)
    expected_end_date = Column(DateTime(timezone=True))
    deletion_progress = Column(Enum(DeletionProgress))
    archive_progress = Column(Enum(ArchiveProgress))
    date_added = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    date_modified = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    date_deleted = Column(TIMESTAMP(timezone=True), default=None, nullable=True)
    date_archived = Column(TIMESTAMP(timezone=True), default=None, nullable=True)
    # date_added = Column(DateTime(timezone=True), nullable=False, default=func.now())
    # date_modified = Column(DateTime(timezone=True), server_default=func.now(),
    #                        onupdate=func.now(), nullable=False)
    # date_deleted = Column(DateTime, default=None, nullable=True)
    # date_archived = Column(DateTime, default=None, nullable=True)
    notes = Column(String(255))

    #### Establishing the relationship with md5_verify_queue
    # md5_verify_queues = relationship('md5VerifyQueue', back_populates='wb_project')