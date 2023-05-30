import os
import pytest
from dotenv import load_dotenv
from utils.helper import BaseSession


load_dotenv()

REQRES_URL = os.getenv('reqres_base_url')  # потом убрать это для примера
BOOKER_URL = os.getenv('booker_base_url')


@pytest.fixture(scope="session")
def booker(allure_attachments_flag=1):
    with BaseSession(base_url=BOOKER_URL) as session:
        yield session


@pytest.fixture(scope="session")  # это для примера
def reqres():
    with BaseSession(base_url=REQRES_URL) as session:
        yield session
