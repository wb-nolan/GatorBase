from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import wb_projects as wb_projects_schemas
from schemas.wb_projects import WbProjectCreate, WbProjectUpdate
from helper import convert_dates

router = APIRouter()


def create_wb_project(db: Session, project: WbProjectCreate):
    db_project = WbProjects(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_wb_project(db: Session, project_id: int):
    return db.query(WbProjects).filter(WbProjects.id == project_id).first()

def get_wb_projects(db: Session, skip: int = 0):  # , limit: int =10):
    return db.query(WbProjects).offset(skip).all()  # .limit(limit).all()


def update_wb_project(db: Session, project_id: int, project: WbProjectUpdate):
    db_project = db.query(WbProjects).filter(
        WbProjects.id == project_id).first()
    if db_project:
        update_data = project.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project

@router.post("/", response_model=wb_projects_schemas.WbProjectResponse)
def create_wb_project(project: wb_projects_schemas.WbProjectCreate, db: Session = Depends(get_db)):
    return create_wb_project(db, project)


@router.get("/{wb_project_id}", response_model=wb_projects_schemas.WbProjectResponse)
# @router.get("/wb_projects/{wb_project_id}", response_model=str)
def read_wb_project(wb_project_id: int, db: Session = Depends(get_db)):


    
    db_project = get_wb_project(db, wb_project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project Not Found")
    convert_dates(db_project)
    return db_project
    # return db_project.proj_name


@router.get("/", response_model=list[wb_projects_schemas.WbProjectResponse])
def read_all_projects(db: Session = Depends(get_db)):

    db_projects = get_wb_projects(db)
    for db_project in db_projects:
        convert_dates(db_project)
    return db_projects

@router.put("/{wb_project_id}", response_model=wb_projects_schemas.WbProjectUpdate)
def update_wb_project(wb_project_id: int, wb_project: wb_projects_schemas.WbProjectUpdate, db: Session = Depends(get_db)):
    db_project = get_wb_project(db, wb_project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail='Project Not Found')
    updated_wb_project = update_wb_project(db, wb_project_id, wb_project)
    return updated_wb_project


@router.delete("/del/{wb_project_id}", response_model=dict)
def delete_wb_project(wb_project_id: int, db: Session = Depends(get_db)):

    wb_project = db.query(models.wb_projects.WbProjects).filter(models.wb_projects.WbProjects.id == wb_project_id).first()
    if not wb_project:
        raise HTTPException(status_code=404, detail="Project Not Found")
    db.delete(wb_project)
    db.commit()
    return {"detail": "Project deleted successfully"}

# @router.get("/search", response_model=list[wb_projects_schemas.WbProjectResponse])
# def search_projects(
#     active: str = Query(None, description="Is Active Yes or No"),
#     name: str = Query(None, description="Name to Filter"),
    
# )