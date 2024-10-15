import requests
import logging

from models.schema_post_booking import BookingData
from configurations import POST_BOOKING_URL

logger = logging.getLogger('api')


class PostBooking:
    def __init__(self, url: str):
        self.url = url

    def post_booking(self, body: dict):
        req = requests.post(url=POST_BOOKING_URL, json=body)
        try:
            data = BookingData(**req.json())
            logger.info(data)
        except ValueError as e:
            logger.info(f'Validation error: {e}')
        return req
