from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
import models.wb_projects
from schemas import wb_projects as wb_projects_schemas
from crud import wb_projects as wb_projects_crud

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cors import add_cors

models.wb_projects.Base.metadata.create_all(bind=engine)
# models.category.Base.metadata.create_all(bind=engine)

app = FastAPI()
add_cors(app)

@app.post("/wb_projects/", response_model=wb_projects_schemas.WbProjectResponse)
def create_wb_project(project: wb_projects_schemas.WbProjectCreate, db: Session = Depends(get_db)):
    return wb_projects_crud.create_wb_project(db, project)

@app.get("/wb_projects/{wb_project_id}", response_model=wb_projects_schemas.WbProjectResponse)
def read_wb_project(wb_project_id: int, db: Session = Depends(get_db)):
    db_project = wb_projects_crud.get_wb_project(db, wb_project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project Not Found")
    return db_project

@app.delete("/wb_projects/del/{wb_project_id}", response_model=dict)
def delete_wb_project(wb_project_id: int, db: Session = Depends(get_db)):

    wb_project = db.query(models.wb_projects.WbProjects).filter(models.wb_projects.WbProjects.id == wb_project_id).first()
    if not wb_project:
        raise HTTPException(status_code=404, detail="Project Not Found")
    db.delete(wb_project)
    db.commit()

    return {"detail": "Project deleted successfully"}