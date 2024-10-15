import allure

from register.post_body import post_body
from register.post_booking_api import PostBooking
from configurations import POST_BOOKING_URL

@allure.title("Test Post Booking")
@allure.description("Creates a new booking in the API")
class TestPostBooking:
    def test_post_booking(self):
        response = PostBooking(url=POST_BOOKING_URL).post_booking(body=post_body)
        assert response.status_code == 200
