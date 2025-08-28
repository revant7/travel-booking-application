# 🌍 Travel Booking Application

An end-to-end **Travel Booking Platform** developed with **Django** and **MySQL**, designed to streamline the process of exploring travel options, booking tickets, and managing reservations.  

The project showcases **full-stack development skills** including authentication, relational database design, booking workflows, and deployment on Railway.  
It was implemented as part of an academic assignment but structured to reflect **real-world, production-ready practices**.

🔗 **Live Demo** → [Travel Booking Application](https://travel-booking-application-production.up.railway.app/)

---

## ✨ Key Highlights
- **User-Centric Experience** → Registration, authentication, profile management
- **Travel Options Module** → Dynamic listing of flights, trains, and buses with filters
- **Booking Engine** → Seat availability checks, price calculation, booking confirmations
- **Booking Lifecycle** → Users can review, manage, and cancel bookings
- **Secure & Reliable** → Built on Django’s authentication & CSRF protection
- **Production Deployment** → Hosted on Railway with MySQL integration
- **Clean UI/UX** → Responsive pages styled with Bootstrap & CSS

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** Django Templates + Bootstrap 5
- **Database:** MySQL
- **Deployment:** Railway
- **Version Control:** Git & GitHub


## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/travel-booking-app.git
cd travel-booking-app
```
### 2. Backend Setup
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Database Setup

Create a MySQL database
Configure .env with DB credentials:

```bash
DB_NAME=travel_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306

#Run:
python manage.py makemigrations
python manage.py migrate
```

### Deployment
Application deployed on Railway

Environment variables stored securely

Supports production-ready settings with dev and prod configurations

## 👨‍💻 Author

**Revant Khanna**  
📌 [GitHub](https://github.com/revantkhanna) | 🔗 [LinkedIn](https://www.linkedin.com/in/revant-khanna)

