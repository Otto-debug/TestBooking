import requests
import logging

from configurations import GET_BOOKING_URL

logger = logging.getLogger('delete api')

class DeleteBooking:
    def __init__(self, url: str):
        self.url = url

    def delete_booking(self, headers: dict):
        response = requests.delete(url=GET_BOOKING_URL, headers=headers)
        logger.info(response.text)
        return response