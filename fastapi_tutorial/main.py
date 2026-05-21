from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory student storage
students = [
    {"id": 1, "name": "nikita", "city": "sundernagar"},
    {"id": 2, "name": "saurabh", "city": "solan"},
    {"id": 3, "name": "palak", "city": "Hamirpur"},
]

class Student(BaseModel):
    id: int
    name: str
    city: str

# GET /
@app.get("/")
def home():
    return {"message": "Welcome to my first API"}

# GET /students
@app.get("/students")
def get_students():
    return {"total": len(students), "students": students}

# POST /students  → add one student
@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())
    return {"message": "Student created", "student": student}

# PUT /students/{student_id}  → update one student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):
    for i, s in enumerate(students):
        if s["id"] == student_id:
            students[i] = updated.model_dump()
            return {"message": "Student updated", "student": updated}
    raise HTTPException(status_code=404, detail="Student not found")

# DELETE /students/{student_id}  → delete one student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, s in enumerate(students):
        if s["id"] == student_id:
            removed = students.pop(i)
            return {"message": "Student deleted", "student": removed}
    raise HTTPException(status_code=404, detail="Student not found")