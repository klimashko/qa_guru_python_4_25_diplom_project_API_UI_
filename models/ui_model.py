import os

from faker import Faker
from dotenv import load_dotenv

load_dotenv()
fake_data = Faker()


class FakeClient:
    @staticmethod
    def message_data():
        name = fake_data.name()
        phone = fake_data.msisdn()
        email = fake_data.email()
        # subject = fake_data.word()
        subject = fake_data.lexify('?' * 7)
        message = fake_data.text()

        return {
             "name": name,
             "phone": phone,
             "email": email,
             "subject": subject,
             "message": message
        }
def check():
    client_data = FakeClient.message_data()
    print(client_data)
    print(client_data.get('name'))
    print(client_data.get('subject'))


check()


