import allure

from register.get_booking_api import GetBooking

from configurations import GET_BOOKING_URL

@allure.title("Test Get Booking")
@allure.description("Returns a specific booking based upon the booking id provided")
class TestGetBooking:
    def test_get_booking(self):
        response = GetBooking(GET_BOOKING_URL).get_booking()
        assert response.status_code == 200