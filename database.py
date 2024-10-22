from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

 DATABASE_URL = 'mysql+mysqlconnector://wbapps:pw4apps@alfred-01/alfred_mpi'
 DEV_DATABASE_URL = 'mysql://root@localhost:3306/alfred_mpi' 
engine = create_engine(DEV_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
