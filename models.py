# models/models.py
from enum import Enum
from pydantic import BaseModel, EmailStr

class TechKnowledge(str, Enum):
    beginner = "Beginner"
    intermediate = "Intermediate"
    advanced = "Advanced"

class Course(str, Enum):
    graphic_design = "Graphic Design"
    web_design = "Web Design"
    computer_basics = "Computer Basics"

class AttendanceDays(str, Enum):
    mwf = "MWF"
    tth = "TTH"
    fs = "FS"

class StudentsForm(BaseModel):
    first_name: str
    last_name: str
    middle_name: str = ''
    date_of_birth: str
    tech_knowledge: TechKnowledge
    select_course: Course
    preferred_attendance_days: AttendanceDays
    email_address: EmailStr
    phone_number: str
    home_address: str
    
    
    class Config:
        json_schema_extra = {
            "examples": [
                {
            "first_name": "John",
            "last_name": "Doe",
            "date_of_birth": "1990-01-01",
            "tech_knowledge": "Intermediate",
            "select_course": "Graphic Design",
            "preferred_attendance_days": "MWF",
            "email_address": "john.doe@example.com",
            "phone_number": "1234567890",
            "home_address": "123 Main Street",
                },
            ]
        }
