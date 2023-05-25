import os
import pytest
from dotenv import load_dotenv

from utils.helper import BaseSession

load_dotenv()

REQRES_URL = os.getenv('reqres_base_url')


@pytest.fixture(scope="session")
def reqres():
    with BaseSession(base_url=REQRES_URL) as session:
        yield session