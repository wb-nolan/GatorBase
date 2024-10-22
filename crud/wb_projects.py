from sqlalchemy.orm import Session
from models.wb_projects import WbProjects
from schemas.wb_projects import WbProjectCreate, WbProjectUpdate

def create_wb_project(db: Session, project: WbProjectCreate):
    db_project = WbProjects(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_wb_project(db: Session, project_id: int):
    return db.query(WbProjects).filter(WbProjects.id == project_id).first()

def get_wb_projects(db: Session, skip: int=0):#, limit: int =10):
    return db.query(WbProjects).offset(skip).all()#.limit(limit).all()

def update_wb_project(db: Session, project_id: int, project: WbProjectUpdate):
    db_project = db.query(WbProjects).filter(WbProjects.id == project_id).first()
    if db_project:
        update_data = project.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project