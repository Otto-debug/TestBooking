import requests
import logging

from models.schema_get_booking import Booking
from configurations import GET_BOOKING_URL

logger = logging.getLogger('api')

class GetBooking:
    def __init__(self, url: str):
        self.url = url

    def get_booking(self):
        response = requests.get(url=GET_BOOKING_URL)
        try:
            data = Booking(**response.json())
            logger.info(data)
        except ValueError as e:
            logger.info(f'Validation error: {e}')
        return response
