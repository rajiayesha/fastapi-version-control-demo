from fastapi import FastAPI

app = FastAPI(title="Course Management API")

@app.get("/")
def read_root():
    return {"message": "Course Management API is running"}

@app.get("/courses")
def list_courses():
    return {
        "courses": [
            {"id": 1, "title": "Backend API Fundamentals"},
            {"id": 2, "title": "FastAPI Application Fundamentals"}
        ]
    }