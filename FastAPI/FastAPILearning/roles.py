from sqlalchemy import Column, Integer, String
from database import Base
 
class Roles(Base):
    __tablename__ = "roles"  # Name of the table in PostgreSQL
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)