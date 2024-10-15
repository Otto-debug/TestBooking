import allure

from register.update_booking import UpdateBooking
from register.post_body import post_body
from register.headers import headers

from configurations import GET_BOOKING_URL

@allure.title("Test Update Booking")
@allure.description("Updates a current booking")
class TestUpdateBooking:
    def test_update_booking(self):
        response = UpdateBooking(url=GET_BOOKING_URL).update_booking(body=post_body,
                                                                     headers=headers)
        try:
            assert response.status_code == 200
            print('Booking update successfully!')
        except ValueError as e:
            print(f"Failed to update booking. Status code: {response.status_code}. Error: {e}")
            print(f"Response: {response.text}")