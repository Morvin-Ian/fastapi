from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    grade: int
    major: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[int] = None
    major: Optional[str] = None

students = {
    1:{
        "name": "Morvin Ian",
        "age": 25,
        "grade": 12,
        "major": "Computer Science"
    }, 
    2:{
        "name": "Bernard Todd",
        "age": 24,
        "grade": 11,
        "major": "Mathematics"
    },
    3:{
        "name": "Alfred Johnson",
        "age": 26,
        "grade": 10,
        "major": "Physics"
    }
}

@app.get("/")
async def index():
    return {"Name": "Morvin Ian"}

@app.get("/students")
async def get_students():
    return students

@app.get("/students/{student_id}")
async def get_student(student_id: int = Path(description="Student ID to be viewed")):
    if student_id in students.keys():
        return students[student_id]
    else:
        return {"message": "Student not found"}
    
@app.post("/students")
async def add_student(student: Student):
    global students
    students[len(students)+1] = student
    return students[len(students)]

@app.put("/students/{student_id}/")
async def add_student(student_id: int, student:UpdateStudent):
    global students
    if student_id not in students.keys():
        return {"message": "Student not found"}
    
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.grade != None:
        students[student_id]["grade"] = student.grade
    if student.major != None:
        students[student_id]["major"] = student.major

    students[student_id] = student        
    return students[student_id]