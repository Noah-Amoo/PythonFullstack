import models.student_models as student_models
from models.student_models import StudentPayload
from typing import Optional
from sqlalchemy.orm import Session
from models.student import Student

from fastapi import APIRouter, HTTPException, Depends

from database import get_db
router = APIRouter()

student_data : dict[int, StudentPayload] = {}

@router.post("/{student_name}/", response_model=StudentPayload)
def create_student(
    student_name: str,
    age: int,
    ni_number: str,
    db: Session = Depends(get_db)
) -> Student:
    if age <= 0 or age >= 30:
        raise HTTPException(
            status_code=400,
            detail={"error": "Age must be between 1 and 30"}
        )

    existing_student = db.query(Student).filter(Student.student_name == student_name).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail={"error": "Student name already exists"}
        )

    student = Student(
        student_name=student_name,
        age=age,
        ni_number=ni_number
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student

@router.get("/{student_id}/")
def get_student(student_id: int):
    student = student_data.get(student_id)
    if student:
        return student
    else:
        return HTTPException(status_code=404, detail={"error": "Student not found"})

@router.get("/")  
def get_all_students():
    if not student_data:  # not false {}  it will return true if the dictionary is empty
        return HTTPException(status_code=400, detail={"message": "Enter at least one student"})
    return student_data

@router.put("/{student_id}/")
def update_student(student_id: int, student_name: str, age: int):
    student = student_data.get(student_id)
    if student:
        if age <= 0 or age >= 30:
            return HTTPException(status_code=400, detail={"error": "Age must be between 1 and 30"})
        if student_name in [s.student_name for s in student_data.values() if s.id != student_id]:
            return HTTPException(status_code=400, detail={"error": "Student name already exists"})
        student.student_name = student_name
        student.age = age
        return student
    else:
        return HTTPException(status_code=404, detail={"error": "Student not found"})

@router.delete("/{student_id}/")
def delete_student(student_id: int):
    if student_id in student_data:
        del student_data[student_id]
        return HTTPException(status_code=200, detail={"message": "Student deleted successfully"})
    else:
        return HTTPException(status_code=404, detail={"error": "Student not found"})       