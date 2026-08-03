from sqlalchemy import Column, Integer, String
from database import Base
 
class Student(Base):
    __tablename__ = "students"  # Name of the table in PostgreSQL
 
    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, nullable=False)
    age = Column(Integer)
    ni_number = Column(String, unique=True)




