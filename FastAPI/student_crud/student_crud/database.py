from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# Replace with your actual database username, password, host, and database name
DATABASE_URL = "postgresql://postgres:Nanayawafriyie1989*@localhost:5432/postgres"

 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
 



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()