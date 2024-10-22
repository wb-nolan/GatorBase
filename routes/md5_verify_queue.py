from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import md5_verify_queue as md5_verify_queue_schemas
from crud import md5_verify_queue as md5_verify_queue_crud
from helper import convert_dates
from models.md5_verify_queue import md5VerifyQueue

router = APIRouter()


@router.post("/", response_model=md5_verify_queue_schemas.md5VerifyQueueResponse)
def create_md5_verify(project: md5_verify_queue_schemas.md5VerifyQueueCreate, db: Session = Depends(get_db)):
    return md5_verify_queue_crud.create_md5_verify_queue(db, project)


@router.get("/", response_model=list[md5_verify_queue_schemas.md5VerifyQueueResponse])
def read_all_md5_verifies(db: Session = Depends(get_db)):
    db_md5_verifies = md5_verify_queue_crud.get_all_md5_verify_queue(db)

    for db_md5_verify in db_md5_verifies:
        convert_dates(db_md5_verify)
        
    return db_md5_verifies
    # return db_md5_verify
    

@router.get("/{md5_verify_queue_id}", response_model=md5_verify_queue_schemas.md5VerifyQueueResponse)
# @router.get("/md5_verify_queue/{md5_verify_queue_id}", response_model=str)
def read_md5_verify_queue(md5_verify_queue_id: int, db: Session = Depends(get_db)):
    db_md5_verify = md5_verify_queue_crud.get_md5_verify_queue(db, md5_verify_queue_id)
    if db_md5_verify is None:
        raise HTTPException(status_code=404, detail="Project Not Found")
    convert_dates(db_md5_verify)
    return db_md5_verify
    # return db_md5_verify.proj_name




@router.put("/{md5_verify_queue_id}", response_model=md5_verify_queue_schemas.md5VerifyQueueUpdate)
def update_md5_verify_queue(md5_verify_queue_id: int, md5_verify_queue: md5_verify_queue_schemas.md5VerifyQueueUpdate, db: Session = Depends(get_db)):
    db_md5_verify = md5_verify_queue_crud.get_md5_verify_queue(db, md5_verify_queue_id)
    if db_md5_verify is None:
        raise HTTPException(status_code=404, detail='Project Not Found')
    updated_md5_verify_queue = md5_verify_queue_crud.update_md5_verify_queue(db, md5_verify_queue_id, md5_verify_queue)
    return updated_md5_verify_queue


@router.delete("/del/{md5_verify_queue_id}", response_model=dict)
def delete_md5_verify_queue(md5_verify_queue_id: int, db: Session = Depends(get_db)):
    md5_verify_queue = db.query(md5VerifyQueue).filter(md5VerifyQueue.id == md5_verify_queue_id).first()
    if not md5_verify_queue:
        raise HTTPException(status_code=404, detail="Project Not Found")
    db.delete(md5_verify_queue)
    db.commit()
    return {"detail": "Project deleted successfully"}