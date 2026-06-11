from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 1, "name": "Tanmay", "department": "IT"},
    {"id": 2, "name": "Rahul", "department": "HR"}
]

@app.get("/")
def home():
    return {"message": "Employee API Running"}

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return {"error": "Employee not found"}

@app.post("/employees")
def add_employee(employee: dict):
    employees.append(employee)
    return {"message": "Employee added", "employee": employee}