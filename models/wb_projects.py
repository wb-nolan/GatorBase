from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class DeletionProgress(str, Enum):
    PENDING = 'PENDING'
    READY = 'READY'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

class ArchiveProgress(str, Enum):
    PENDING = 'PENDING'
    READY_FOR_ARCHIVE = 'READY_FOR_ARCHIVE'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

class wb_projects(Base):
    __tablename__ = 'wb_projects'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(11))
    fileset = Column(Integer)
    active = Column(Boolean) ### CHANGED
    in_alfred = Column(Boolean) ### CHANGED
    proj_name = Column(String(50)), unique=True) # ADDED Unique
    studio = Column(String(255))
    archivebarcode = Column(String(11))
    lto = Column(String(11)) 
    proj_path = Column(String(255))
    proj_size = Column(Integer)
    proj_size_gb = Column(Integer)
    expected_end_date = Column(DateTime(timezone=True))
    deletion_progress = Column(Enum(DeletionProgress))
    archive_progress = Column(Enum(ArchiveProgress))
    date_added = Column(DateTime(timezone=True), nullable=False, default=func.now())
    date_modified = Column(DateTime(timezone=True), server_default=func.now(),
                           onupdate=func.now(), nullable=False)
    date_deleted = Column(DateTime, default=None, nullable=True)
    date_archived = Column(DateTime, default=None, nullable=True)
    notes = Column(String(255))

    #### Establishing the relationship with md5_verify_queue
    md5_verify = relationship('md5_verify_queue', back_populates='wb_project')