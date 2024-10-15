import allure

from register.delete_booking import DeleteBooking
from register.headers import headers

from configurations import GET_BOOKING_URL


@allure.title("Test Delete Booking")
@allure.description(
    "Returns the ids of all the bookings that exist within the API. "
    "Can take optional query strings to search and return a subset of booking ids.")
class TestDeleteBooking:
    def test_delete_booking(self):
        response = DeleteBooking(url=GET_BOOKING_URL).delete_booking(headers=headers)
        try:
            assert response.status_code == 201
            print('Booking deleted successfully!')
        except ValueError as e:
            print(f"Failed to delete booking. Status code: {response.status_code}. Error: {e}")
            print(f"Response: {response.text}")
