import os

from faker import Faker
from dotenv import load_dotenv

load_dotenv()
fake_data = Faker()


class BookingData:
    @staticmethod
    def payload_data():
        firstname = fake_data.first_name()
        lastname = fake_data.last_name()
        totalprice = fake_data.random_int(min=100, max=900)
        depositpaid = fake_data.boolean()
        checkin = fake_data.date()
        checkout = fake_data.date()
        additionalneeds = fake_data.bothify()

        return {
            'firstname': firstname,
            'lastname': lastname,
            'totalprice': totalprice,
            'depositpaid': depositpaid,
            'bookingdates':
                {
                    'checkin': checkin,
                    'checkout': checkout
                },
            'additionalneeds': additionalneeds
        }

    @staticmethod
    def payload_data_short():
        firstname = fake_data.first_name()
        lastname = fake_data.last_name()

        return {
            'firstname': firstname,
            'lastname': lastname,
        }

    @staticmethod
    def headers_data():
        AUTHORIZATION = os.getenv('authorization')
        content_type = "application/json"
        accept = "application/json"

        return {
            "Content-Type": content_type,
            "Accept": accept,
            "Authorization": AUTHORIZATION
        }
