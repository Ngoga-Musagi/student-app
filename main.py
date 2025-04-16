from fastapi import FastAPI, HTTPException
from typing import List
from models import Student

app = FastAPI()
students: List[Student] = []

@app.post("/students/")
def create_student(student: Student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student with this ID already exists.")
    students.append(student)
    return student

@app.get("/students/", response_model=List[Student])
def get_all_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found.")

@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Student not found.")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            students.pop(i)
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found.")
