from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/addGatorExcelToAlfred_APP/API/')
from routes import wb_projects, md5_verify_queue, gator
from database import engine
import models.wb_projects
from cors import add_cors


app = FastAPI(root_path="/api")
add_cors(app)


app.include_router(gator.router, prefix='/gator', tags=["gator"])
app.include_router(wb_projects.router, prefix="/wb_projects", tags=["wb_projects"])
app.include_router(md5_verify_queue.router, prefix="/md5_verify_queue", tags=["md5_verify_queue"])

models.wb_projects.Base.metadata.create_all(bind=engine)
models.md5_verify_queue.Base.metadata.create_all(bind=engine)


