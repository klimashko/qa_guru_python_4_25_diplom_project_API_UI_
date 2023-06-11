import os

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

'''Убрать вспомогательную ф-ию check()!!!!!!!!!!!!!!!!!'''
def check():
    client_data = UserMessage.message_data()
    print(client_data)
    print(client_data.get('name'))
    print(client_data.get('subject'))
    print(client_data.get("phone"))


check()

# class HotelRoom:
#     @staticmethod
#     def hotel_room_features():
