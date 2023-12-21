from fastapi import APIRouter
from db import create_students_table, insert_student_data
from models import StudentsForm

router = APIRouter()

@router.post("/students/")
def create_student(student_form: StudentsForm):
    insert_student_data(student_form)
    return {"message": "Student data inserted successfully!"}

@router.post("/create-table/")
def create_students_table_endpoint():
    create_students_table()
    return {"message": "You have already register!"}
