# Expense Tracker

A personal expense tracking web application built with Python and Django.

## Live Demo
https://expense-tracker-a471.onrender.com

## Features
- Secure login and logout authentication
- Add, edit and delete expenses
- Dashboard with live stats — total spent, monthly total, biggest expense
- Category-wise pie chart using Chart.js
- CSV export to download all expenses
- Responsive UI with Bootstrap 5

## Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Charts:** Chart.js

## Setup Instructions
1. Clone the repo
   git clone https://github.com/YOURUSERNAME/expense-tracker.git
2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies
   pip install -r requirements.txt
4. Run migrations
   python manage.py migrate
5. Create superuser
   python manage.py createsuperuser
6. Run the server
   python manage.py runserver
