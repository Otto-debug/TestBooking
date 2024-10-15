import requests
import logging

from models.schema_get_bookingIds import BookingIdList
from configurations import GET_BOOKING_IDS_URL

logger = logging.getLogger('api')


class GetBookingIds:
    def __init__(self, url: str):
        self.url = url

    def get_bookingIds(self):
        response = requests.get(url=GET_BOOKING_IDS_URL)
        try:
            booking = BookingIdList(response.json())
            logger.info(booking)
        except ValueError as e:
            logger.info(f'Validation error: {e}')
        return response
