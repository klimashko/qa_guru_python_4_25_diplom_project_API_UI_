import json
import logging

import allure
import curlify
from allure import step
from requests import Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        with step(f'{method} {url}'):
            response = super().request(method=method, url=f'{self.base_url}{url}',
                                       **kwargs)

            """Логирование request curl с кодом ответа и текстом response"""
            logging.info(
                f"Status code: {response.status_code} {curlify.to_curl(response.request)}")
            logging.info(response.text)

            """Добавление в allure attachments: request curl с кодом ответа и response, в зависимости от его типа """
            allure.attach(
                f"Status code: {response.status_code} {curlify.to_curl(response.request)}",
                name="Text", attachment_type=allure.attachment_type.TEXT)

            content_type = response.headers.get('Content-Type')
            if content_type and isinstance(content_type, str):
                content_type = content_type.split(';')[0].strip()
            else:
                content_type = type(content_type).__name__

            if content_type == 'application/json':
                allure.attach(json.dumps(response.json(), indent=4), 'JSON response',
                              allure.attachment_type.JSON)
            elif content_type == 'text/plain':
                allure.attach(response.text, 'Text response',
                              allure.attachment_type.TEXT)
            else:
                allure.attach(response.content, 'Unknown response',
                              allure.attachment_type.TEXT)

        return response
