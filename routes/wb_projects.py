from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import wb_projects as wb_projects_schemas
from crud import wb_projects as wb_projects_crud
from helper import convert_dates

router = APIRouter()


@router.post("/", response_model=wb_projects_schemas.WbProjectResponse)
def create_wb_project(project: wb_projects_schemas.WbProjectCreate, db: Session = Depends(get_db)):
    return wb_projects_crud.create_wb_project(db, project)


@router.get("/{wb_project_id}", response_model=wb_projects_schemas.WbProjectResponse)
# @router.get("/wb_projects/{wb_project_id}", response_model=str)
def read_wb_project(wb_project_id: int, db: Session = Depends(get_db)):
    db_project = wb_projects_crud.get_wb_project(db, wb_project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project Not Found")
    convert_dates(db_project)
    return db_project
    # return db_project.proj_name


@router.get("/", response_model=list[wb_projects_schemas.WbProjectResponse])
def read_all_projects(db: Session = Depends(get_db)):
    db_projects = wb_projects_crud.get_wb_projects(db)
    for db_project in db_projects:
        convert_dates(db_project)
    return db_projects

@router.put("/{wb_project_id}", response_model=wb_projects_schemas.WbProjectUpdate)
def update_wb_project(wb_project_id: int, wb_project: wb_projects_schemas.WbProjectUpdate, db: Session = Depends(get_db)):
    db_project = wb_projects_crud.get_wb_project(db, wb_project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail='Project Not Found')
    updated_wb_project = wb_projects_crud.update_wb_project(db, wb_project_id, wb_project)
    return updated_wb_project


@router.delete("/del/{wb_project_id}", response_model=dict)
def delete_wb_project(wb_project_id: int, db: Session = Depends(get_db)):

    wb_project = db.query(models.wb_projects.WbProjects).filter(models.wb_projects.WbProjects.id == wb_project_id).first()
    if not wb_project:
        raise HTTPException(status_code=404, detail="Project Not Found")
    db.delete(wb_project)
    db.commit()
    return {"detail": "Project deleted successfully"}