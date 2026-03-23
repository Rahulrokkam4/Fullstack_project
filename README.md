# 🚚 Logistics Tracker

A full-stack web application for tracking, managing, and updating logistics data in real-time.
Built with a modern tech stack including **React.js (Frontend)**, **FastAPI (Backend)**, and **PostgreSQL (Database)**.

---

## 📖 Overview

The **Logistics Tracker** helps users efficiently manage logistics records by providing direct database interaction through a user-friendly interface.

Users can:

* Track logistics data in real-time
* Perform CRUD operations (Create, Read, Update, Delete)
* Easily manage records via an interactive UI

---

## 🚀 Features

* 📊 Real-time logistics tracking
* ➕ Add new records
* ✏️ Edit and update existing data
* ❌ Delete records
* 🔄 Seamless backend–database integration
* ⚡ Fast API responses using FastAPI
* ✅ Data validation using Pydantic

---

## 🛠 Tech Stack

### Frontend

* React.js
* JavaScript
* HTML5
* CSS3

### Backend

* FastAPI (Python)
* SQLAlchemy (ORM)
* Pydantic (Data validation)

### Database

* PostgreSQL
* psycopg2 (Database adapter)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rahulrokkam4/Fullstack_project.git
```

---

### 2️⃣ Setup Backend

```bash
# Create virtual environment
python -m venv venv

# Activate venv
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r rqt.txt
```

---

### 3️⃣ Run Backend Server

```bash
# Navigate to frontend folder
cd Backend

uvicorn main:app --reload
```

Backend will run at:
👉 http://127.0.0.1:8000

---

### 4️⃣ Setup Frontend

```bash
# Install Node.js (if not installed)

# Navigate to frontend folder
cd Frontend

# Install dependencies
npm install

# Run React app
npm start
```

Frontend will run at:
👉 http://localhost:3000

---

## 📂 Project Structure

```
logistics-tracker/
│
├── venv/
├── backend/
│   ├── data_init.py
│   ├── datavalidation.py
│   ├── db_config.py
│   ├── db_model.py
│   ├── main.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│
├── rqt.txt
└── README.md
```

---

## 🔌 API Overview

The backend provides RESTful APIs using FastAPI:

* `GET /` → Fetch all records
* `POST /` → Add new logistics data
* `PUT /{id}` → Update record
* `DELETE /{id}` → Delete record

---

## 🧪 Example Workflow

1. Open the frontend UI
2. Add a new logistics record
3. Edit or update existing entries
4. Delete unwanted data
5. Changes are instantly reflected in PostgreSQL

---

## 🧠 Architecture Overview
## 🧠 System Architecture

```
                        🌐 User (Browser)
                                │
                                ▼
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │ (HTML, CSS, JS)     │
                    └─────────┬───────────┘
                              │
                 HTTP Requests │ (REST API)
                              ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    │   (Python, Uvicorn) │
                    └─────────┬───────────┘
                              │
             ORM (SQLAlchemy) │
                              ▼
                    ┌─────────────────────┐
                    │   PostgreSQL DB     │
                    │   (psycopg2)        │
                    └─────────────────────┘


🔁 Flow Explanation:

1. User interacts with the React UI (Add / Edit / Delete / View)
2. React sends HTTP requests to FastAPI endpoints
3. FastAPI processes the request using Pydantic validation
4. SQLAlchemy ORM converts Python objects → SQL queries
5. PostgreSQL executes queries and returns data
6. FastAPI sends response back to frontend
7. UI updates in real-time
```

---

## 🔄 Request Flow (Step-by-Step)

```
User Action → React → API Call → FastAPI → SQLAlchemy → PostgreSQL
      ↑                                                     ↓
      └────────────── Response (JSON) ←─────────────────────┘
```

---

## 🧩 Component Breakdown

* **Frontend (React)**

  * UI rendering
  * Form handling (Add / Update)
  * API integration (fetch/axios)

* **Backend (FastAPI)**

  * REST API endpoints
  * Business logic
  * Data validation (Pydantic)

* **Database Layer**

  * SQLAlchemy ORM
  * PostgreSQL storage
  * psycopg2 connection

---

## ⚡ Deployment Architecture (Future Scope)

```
React (Frontend) → Nginx → FastAPI (Gunicorn/Uvicorn) → PostgreSQL
```


## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📌 Future Improvements

* 🔐 Authentication & Authorization
* 📈 Dashboard with analytics
* 🌐 Deployment (Docker + Cloud)
* 🔔 Real-time notifications

---

## 🙌 Acknowledgements

* FastAPI
* React.js
* PostgreSQL

---

⭐ If you like this project, consider giving it a star!
