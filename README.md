# Bus Ticket Booking System

A web-based bus reservation portal built with Django. Users can search for routes, view available buses and seat arrangements, book tickets, and view generated booking details.

---

## Tech Stack
- **Framework:** Django (Python)
- **Database:** SQLite (default for local development)
- **Frontend:** Django Templates, HTML5, CSS3

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/ksav1705/online_bus_booking_system.git
cd bus-ticket-booking-system
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Create an administrative user (optional)
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
```