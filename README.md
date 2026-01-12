# Student API - Django REST Framework

A simple CRUD API for managing students built with Django REST Framework.

## Project Structure

```
student_api/
├── manage.py
├── requirements.txt
├── student_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── students/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    └── views.py
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional - for Admin Panel)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/students/` | List all students |
| POST | `/api/students/` | Create a new student |
| GET | `/api/students/{id}/` | Get student details |
| PUT | `/api/students/{id}/` | Update student (full) |
| PATCH | `/api/students/{id}/` | Update student (partial) |
| DELETE | `/api/students/{id}/` | Delete student |
| GET | `/api/students/active/` | List only active students |

---

## API Usage Examples (cURL)

### Create a Student

```bash
curl -X POST http://127.0.0.1:8000/api/students/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Rahul",
    "last_name": "Sharma",
    "email": "rahul.sharma@example.com",
    "phone": "9876543210",
    "date_of_birth": "2000-05-15",
    "gender": "M",
    "course": "B.Tech Computer Science",
    "address": "Mumbai, Maharashtra"
  }'
```

### Get All Students

```bash
curl http://127.0.0.1:8000/api/students/
```

### Get Single Student

```bash
curl http://127.0.0.1:8000/api/students/1/
```

### Update Student (Full Update)

```bash
curl -X PUT http://127.0.0.1:8000/api/students/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Rahul",
    "last_name": "Sharma",
    "email": "rahul.updated@example.com",
    "phone": "9876543210",
    "course": "M.Tech Computer Science"
  }'
```

### Update Student (Partial Update)

```bash
curl -X PATCH http://127.0.0.1:8000/api/students/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "grade": "A+"
  }'
```

### Delete Student

```bash
curl -X DELETE http://127.0.0.1:8000/api/students/1/
```

### Search Students

```bash
curl "http://127.0.0.1:8000/api/students/?search=rahul"
```

### Get Active Students Only

```bash
curl http://127.0.0.1:8000/api/students/active/
```

---

## Student Model Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| first_name | string | Yes | Student's first name |
| last_name | string | Yes | Student's last name |
| email | string | Yes | Unique email address |
| phone | string | No | Contact number |
| date_of_birth | date | No | Format: YYYY-MM-DD |
| gender | string | No | M, F, or O |
| address | string | No | Full address |
| course | string | No | Enrolled course |
| grade | string | No | Current grade |
| is_active | boolean | No | Default: true |

---

## Features

- Full CRUD operations
- Pagination (10 items per page)
- Search by name, email, course
- Ordering by multiple fields
- Custom action for active students
- Django Admin panel support
- Browsable API (DRF default)

---

## Admin Panel

Access at: `http://127.0.0.1:8000/admin/`

Use the superuser credentials created during setup.
