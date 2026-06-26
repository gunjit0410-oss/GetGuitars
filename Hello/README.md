# 🎸 Get-Guitars

A modern Guitar Store website built using **Django**, **Python**, **HTML**, **CSS**, and **Bootstrap**. The project allows users to browse different categories of guitars and accessories, search for products, submit contact queries, and also provides REST API endpoints for guitar data.

---

## 📌 Features

- 🎸 Browse different guitar categories
  - Acoustic Guitars
  - Electric Guitars
  - Bass Guitars
  - Ukuleles

- 🎵 Guitar Accessories
  - Guitar Covers
  - Strings & Picks
  - Guitar Straps
  - Amplifiers

- 🔍 Search functionality to find guitars by name or brand

- 🛒 Buy buttons that redirect users to Amazon and Flipkart

- 📩 Contact form for customer queries

- 🌐 REST API endpoints for retrieving guitar information and submitting contact requests

- 📱 Fully responsive UI using Bootstrap

---

## 🛠️ Tech Stack

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite3
- Git & GitHub

---

## 📂 Project Structure

```
Get-Guitars/
│
├── Hello/
│   ├── home/
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   └── db.sqlite3
│
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Get-Guitars.git
```

### 2. Go to the project directory

```bash
cd Get-Guitars/Hello
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

Visit

```
http://127.0.0.1:8000/
```

---

## 📡 API Endpoints

The project includes simple REST API endpoints for accessing guitar data and submitting contact information.

### Get all guitars

```
GET /api/guitars/
```

### Get guitar by ID

```
GET /api/guitars/<id>/
```

### Submit Contact Form

```
POST /api/contact/
```

Example JSON

```json
{
    "name": "John Doe",
    "phone": "9876543210",
    "email": "john@example.com",
    "desc": "I want to know about Yamaha guitars."
}
```

---

## 🧪 Testing

Run all test cases

```bash
python manage.py test
```

The project contains tests for

- Guitar API
- Contact API
- Search Functionality

---

## 📸 Screenshots

### Home Page

_Add screenshot here_

### Acoustic Guitars

_Add screenshot here_

### Electric Guitars

_Add screenshot here_

### Search Page

_Add screenshot here_

### Contact Page

_Add screenshot here_

---

## 📚 What I Learned

During this project I learned

- Django project structure
- Django Models
- URL Routing
- Template Inheritance
- Bootstrap Integration
- Static Files
- Forms Handling
- Database Operations
- Native REST APIs using Django
- Writing Unit Tests
- Git & GitHub
- Responsive Web Design

---

## 🔮 Future Improvements

- User Authentication
- Shopping Cart
- Wishlist
- Online Payment Gateway
- Product Reviews & Ratings
- Admin Dashboard
- Product Filters
- Pagination
- Product Comparison
- Deployment on Render

---

## 👨‍💻 Author

**Gunjit verma**

GitHub:
https://github.com/gunjit0410-oss

---

## ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.
