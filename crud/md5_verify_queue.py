from sqlalchemy.orm import Session
from models.md5_verify_queue import md5VerifyQueue
from schemas.md5_verify_queue import md5VerifyQueueCreate, md5VerifyQueueUpdate

def create_md5_verify_queue(db: Session, md5_verify: md5VerifyQueueCreate):
    db_md5_verify = md5VerifyQueue(**md5_verify.dict())
    db.add(db_md5_verify)
    db.commit()
    db.refresh(db_md5_verify)
    return db_md5_verify

def get_md5_verify_queue(db: Session, md5_verify_id: int):
    return db.query(md5VerifyQueue).filter(md5VerifyQueue.id == md5_verify_id).first()

def get_all_md5_verify_queue(db: Session, skip: int=0):#, limit: int =10):
    return db.query(md5VerifyQueue).offset(skip).all()#.limit(limit).all()

def update_md5_verify_queue(db: Session, md5_verify_id: int, md5_verify: md5VerifyQueueUpdate):
    db_md5_verify = db.query(md5VerifyQueue).filter(md5VerifyQueue.id == md5_verify_id).first()
    if db_md5_verify:
        update_data = md5_verify.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_md5_verify, key, value)
        db.commit()
        db.refresh(db_md5_verify)
    return db_md5_verify