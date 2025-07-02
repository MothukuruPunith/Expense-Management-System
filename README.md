# 💸 Expense Management System

This is a full-stack Expense Management web application that helps users track and analyze their daily expenses efficiently. Built using FastAPI for the backend and Streamlit for the frontend.

---

## 📁 Project Structure

```
project_expense_manager/
│
├── backend/                 # Backend logic with FastAPI
│   ├── db_helper.py         # MySQL DB logic & query functions
│   └── server.py            # API endpoints using FastAPI
│
├── frontend/                # Streamlit-based frontend
│   ├── add_update.py        # UI to add/update daily expenses
│   ├── analytics_ui_date.py # UI to analyze expenses between dates
│   ├── analytics_ui_month.py# UI to analyze expenses month-wise
│   └── main.py              # Main entry point for the Streamlit app
│
├── tests/                  # Unit tests
│   ├── backend/             # Tests for backend components
│   │   └── test_db_helper.py
│   ├── frontend/            # Placeholder for frontend tests
│   └── conftest.py          # Pytest fixtures/configuration
│
├── requirements.txt         # All project dependencies
└── README.md
```

---

## 🚀 Features

* Add/update daily expenses with category and notes
* View summary of expenses between any two dates
* Visualize expenses by category with percentages
* View monthly expense trends in a bar chart
* FastAPI backend with REST API endpoints
* Streamlit frontend with tabs for interactivity

---

## 🛠️ Technologies Used

### Backend

* **FastAPI**: Web framework for building APIs
* **Pydantic**: Data validation
* **MySQL**: Relational database
* **mysql-connector-python**: MySQL connection driver

### Frontend

* **Streamlit**: For building interactive UI
* **Pandas**: Data manipulation
* **Altair**: Charting library for visualizations
* **Requests**: HTTP calls to backend

### Testing

* **pytest**: For testing backend functions

---

## 📦 Installation & Running

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/project_expense_manager.git
cd project_expense_manager
```

### 2. Setup Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start MySQL Server & Create Database

Ensure MySQL is running and create a database named `expense_manager`.

```sql
CREATE DATABASE expense_manager;
```

Then, run expense_db_creation.sql file in mysql



### 5. Run Backend (FastAPI)

```bash
cd backend
uvicorn server:app --reload
```

Server will run at `http://127.0.0.1:8000`

### 6. Run Frontend (Streamlit)

```bash
cd ../frontend
streamlit run main.py
```

---

## ✅ API Endpoints

| Endpoint           | Method | Description                         |
| ------------------ | ------ | ----------------------------------- |
| `/expenses/{date}` | GET    | Fetch expenses for a given date     |
| `/expenses/{date}` | POST   | Add/update expenses for a date      |
| `/analytics`       | POST   | Get category-wise summary for range |
| `/analytics_month` | GET    | Get summary grouped by month        |

---

## 📄 requirements.txt (important dependencies)

```txt
fastapi==0.110.0
uvicorn==0.27.1
pydantic==2.7.1
streamlit==1.35.0
pandas==2.2.2
requests==2.31.0
altair==5.3.0
mysql-connector-python==9.3.0
pytest==8.2.1
```

---

## 🧪 Running Tests

If you want to test backend logic:

```bash
pytest tests/
```

---

## 👨‍💼 Author

* Name: Punith
* Course: GenAI Project
* Institution: SRM Institute of Science and Technology

---

## 📬 Feedback & Contributions

Feel free to raise issues or suggest improvements via pull requests.

---

## 📌 Note

* Ensure MySQL is running before using the app.
* Data is not persisted in CSV or external APIs, just MySQL.

Happy Tracking 💰
