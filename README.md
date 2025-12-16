# Barber-Shop-Appointment-Booking-System
Full Stack Python mini project – Barber Shop Appointment Booking System with authentication and CRUD


# Barber Shop Appointment Booking System

A mini web application built with **Django** demonstrating authentication, CRUD operations, database integration, PDF generation, pagination, and a clean responsive UI —  developed as part of a Full Stack Python internship assignment.

---

##  Objective

Build a mini web application demonstrating:
- User authentication (signup, login, logout)
- Secure password hashing
- Session-based authentication
- Full CRUD operations
- Database integration with ORM & migrations
- PDF generation from database data
- Clean and responsive UI

---

##  Features Implemented

###  Authentication
- User Signup
- User Login
- Secure password hashing (Django default)
- Session-based authentication
- Logout functionality

###  Appointment Management (CRUD)
- Create appointment
- View appointment list (table view)
- Update appointment
- Delete appointment
- Users can only see their own appointments

###  Admin
- Django Admin Panel enabled
- Superuser can view and manage all appointments

###  PDF Generation
- Download PDF of **all appointments**
- Download PDF of a **single appointment**

###  Filtering & Pagination
- Filter appointments by:
  - Service
  - Date
- Pagination for appointment list

###  UI & UX
- Responsive layout using **Tailwind CSS**
- Clean and modern design
- Footer with social media icons
- Form validation (date, time, phone number)

---
## Technology Stack

- Backend: Django (Python)
- Frontend: HTML, Tailwind CSS
- Database: SQLite
- Authentication: Django Authentication System
- PDF Generation: xhtml2pdf
- Version Control: Git & GitHub


---

##  Project Structure (Simplified)

```
barber_shop_website/
│
├── appointments/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── config/
│   
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   └── appointments/
│   └── authentication/
│   └── base.html  
│   └── landing.html
│
│── venv
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

##  Setup & Run Instructions

### 1️ Clone the Repository
```bash
git clone https://github.com/Asminstha/Barber-Shop-Appointment-Booking-System
cd barber_shop_website
```

### 2️ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️ Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6️ Run Development Server
```bash
python manage.py runserver
```

Visit >>> `http://127.0.0.1:8000/`

---

##  How to Use

1. Sign up as a new user
2. Login
3. Book an appointment
4. View, update, or delete appointments
5. Download appointment PDF
6. Admin can manage all appointments via `/admin/`

---



##  Conclusion

This project fulfills all core and bonus requirements of the internship assignment and demonstrates practical full-stack Django development skills.It demonstrates backend logic, database handling, authentication, UI design, and additional features like PDF export and pagination using Django.

---


**Developed by:** Asmin Shrestha  
