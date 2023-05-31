import os
import pytest
from dotenv import load_dotenv
from utils.helper import BaseSession


load_dotenv()

BOOKER_URL = os.getenv('booker_base_url')


@pytest.fixture(scope="session")
def booker(allure_attachments_flag=1):
    with BaseSession(base_url=BOOKER_URL) as session:
        yield session

