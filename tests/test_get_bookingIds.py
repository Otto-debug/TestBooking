import pytest
import allure

from configurations import GET_BOOKING_URL

from register.get_bookingIds_api import GetBookingIds

@allure.title("Test Get Ids Booking")
@allure.description("Returns the ids of all the bookings that exist within the API. "
                    "Can take optional query strings to search and return a subset of booking ids.")
@pytest.mark.parametrize('status_code', (200, 404, 500))
class TestGetBooking:
    def test_booking(self, status_code):
        response = GetBookingIds(url=GET_BOOKING_URL).get_bookingIds()
        assert response.status_code == status_code
