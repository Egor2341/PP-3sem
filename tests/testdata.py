from datetime import datetime

REGISTER_DATA = {
    "name": "Egor",
    "surname": "Antipin",
    "email": "egor.anti@mail.ru",
    "password": "pass1234"
}

REGISTER_CLIENT_DATA = {
    "name": "Ivan",
    "surname": "Ivanov",
    "email": "ivan.ivanov@mail.ru",
    "password": "1234pass"
}

LOGIN_DATA = {
    "email": "egor.anti@mail.ru",
    "password": "pass1234"
}


LOGIN_CLIENT_DATA = {
    "email": "ivan.ivanov@mail.ru",
    "password": "1234pass"
}

TOUR_DATA = {
    "title": "ChinaTour",
    "description": "Tour tour tour tour tour tour.",
    "price": 100000.00,
    "duration": 7,
    "start": datetime(2025, 4, 20, 9, 30),
    "end": datetime(2025, 4, 27),
    "destination": "China",
    "availability": 100,
}

TOUR_UPD_DATA = {
    "title": "FranceTour",
    "description": "Tour tour tour tour tour tour.",
    "price": 100000.00,
    "duration": 7,
    "start": datetime(2025, 4, 20, 9, 30),
    "end": datetime(2025, 4, 27),
    "destination": "France",
    "availability": 3,
}