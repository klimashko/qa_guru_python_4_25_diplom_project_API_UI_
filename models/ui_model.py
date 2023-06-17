from faker import Faker
from dotenv import load_dotenv

load_dotenv()
fake = Faker()

import dataclasses


@dataclasses.dataclass
class UserMessage:
    name: str
    phone: str
    email: str
    subject: str
    message: str

    @staticmethod
    def message_data():
        name = fake.name()
        phone = fake.msisdn()
        email = fake.email()
        # subject = fake_data.word()
        subject = fake.lexify('?' * 7)
        message = fake.text()

        return {
            "name": name,
            "phone": phone,
            "email": email,
            "subject": subject,
            "message": message
        }


@dataclasses.dataclass
class Room:
    type_room: str
    number: int
    accessible: bool
    price: int
    wifi: bool
    refresh: bool
    safe: bool
    views: bool

    @staticmethod
    def room_features(type_room):  # Choose room type: 'Single', 'Twin', 'Double', 'Family', 'Suite'

        numbers = {'Single': fake.random_int(min=101, max=199), 'Twin': fake.random_int(min=201, max=299),
                   'Double': fake.random_int(min=301, max=399), 'Family': fake.random_int(min=401, max=499),
                   'Suite': fake.random_int(min=501, max=599)}

        prices = {'Single': 100, 'Twin': 250,
                  'Double': 250, 'Family': 300,
                  'Suite': 990}

        type_room = type_room
        number = numbers[type_room]
        accessible = True
        price = prices[type_room]
        wifi = True
        refresh = True
        safe = True
        views = True

        return {
            'type_room': type_room,
            'number': number,
            'accessible': accessible,
            'price': price,
            'wifi': wifi,
            'refresh': refresh,
            'safe': safe,
            'views': views
        }
