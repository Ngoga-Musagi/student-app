# 🎓 Student CRUD API (FastAPI)

A simple and efficient Student Management REST API built using **FastAPI** and **SQLite**. This app allows you to **create**, **view**, **update**, and **delete** student records. It is also **Dockerized** for seamless containerized deployment.

---

## 🚀 Features

- 📝 Register new students
- 📋 View all registered students
- ✏️ Update student information
- ❌ Delete student records
- ⚡ Auto-generated Swagger and Redoc documentation
- 🐳 Docker support for containerization

---

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Language**: Python
- **Database**: SQLite
- **Containerization**: Docker

---

---

## 📦 API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/students`      | Register a new student   |
| GET    | `/students`      | Get all students         |
| PUT    | `/students/{id}` | Update student by ID     |
| DELETE | `/students/{id}` | Delete student by ID     |

---

## 📤 Sample JSON Payload

### 🔹 POST `/students`

{
  "name": "Ng",
  "age": 100,
  "email": "alexis@example.com"
}

## Step 1: Clone the repository

git clone https://github.com/your-username/student-crud-app.git
cd student-crud-app

# Step 2: Create and activate virtual environment

python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate

# Step 3: Install dependencies

pip install -r requirements.txt

# Step 4: Run the FastAPI server

uvicorn main:app --reload

# Step 5: Access the API Docs
Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

🐳 Running the App with Docker
# Step 1: Build Docker image

docker build -t student-crud-app .
# Step 2: Run the container

docker run -d -p 8000:8000 student-crud-app

# Step 3: Access API docs in your browser
Swagger UI: http://localhost:8000/docs
