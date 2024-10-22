from sqlalchemy import Column, Integer, String, ForeignKey, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum as PyEnum

class TaskTypeStatus(str, PyEnum): # Not used due to "-" in MD5_SUM-C
    FULL_VERIFY = 'FULL_VERIFY'
    MD5_SUM_C = 'MD5_SUM-C' 

class VerifyStatus(str, PyEnum):
    NA = 'NA'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'


class Status(str, PyEnum): # combined for CharScan, VerifyStatus, CompareStatus, & Status
    PENDING = 'PENDING'
    READY = 'READY'
    IN_PROGRESS = 'IN_PROGESS'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    ERROR = 'ERROR'
    ON_HOLD = 'ON_HOLD'
    NA = 'NA'
    SUCCESS = 'SUCCESS' 

class md5VerifyQueue(Base):
    __tablename__ = 'md5_verify_queue'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    hostname = Column(String(50))
    char_scan = Column(Enum(Status), nullable=False)
    log = Column(String)
    # task_type = Column(Enum(TaskTypes))
    task_type = Column(String, default=TaskTypeStatus.FULL_VERIFY)
    status = Column(Enum(Status), nullable=False)
    verify_status = Column(Enum('NA','FAILED','SUCCESS'), nullable=False, default='NA') ### TODO CHECK FOR ENUMs
    compare_status = Column(Enum(Status), nullable=False, default=Status.PENDING) ### TODO CHECK FOR ENUMs
    progress = Column(String(255))
    eta = Column(String(50))
    proj_name = Column(String(50)) # Change to FK - wb_projects #
    # proj_name = Column(String(50), ForeignKey('wb_projects.proj_name'))
    md5_path = Column(String(255))
    md5_name = Column(String(255))
    md5_size = Column(String(15))
    src_count = Column(Integer)
    md5_count = Column(Integer)
    verify_md5_count = Column(Integer)
    compare_md5_count = Column(Integer)
    verify_md5_name = Column(String(255))
    verify_md5_path = Column(String(255))
    compare_md5_path = Column(String(255))
    compare_md5_name = Column(String(255))
    src_name = Column(String(255))
    src_path = Column(String(255))
    src_size = Column(String(25))
    date_added = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    date_modified = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    date_completed = Column(TIMESTAMP(timezone=True), default=None, nullable=True)
    date_started = Column(TIMESTAMP(timezone=True), default=None, nullable=True)
    
    ###### Establishing the relationship with wb_projects
    # wb_project = relationship('WbProjects', back_populates='md5_verify_queues')

