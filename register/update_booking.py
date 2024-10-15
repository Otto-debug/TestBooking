import requests
import logging

from configurations import GET_BOOKING_URL

logger = logging.getLogger('update api')

class UpdateBooking:
    def __init__(self, url: str):
        self.url = url

    def update_booking(self, body: dict, headers: dict):
        response = requests.put(url=GET_BOOKING_URL, json=body, headers=headers)
        logger.info(response.text)
        return response