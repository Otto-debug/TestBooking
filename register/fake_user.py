from faker import Faker
import random

fake = Faker()


class FakeUser:
    """
    FakeUser генерирует фейковые данные
    """
    @staticmethod
    def random_fake_user():
        id = random.randint(1, 10)
        username = fake.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        user_status = random.randint(1, 10)

        return {
            'id': id,
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'phone': phone,
            'user_status': user_status
        }

class FakeCreateBooking:
    """Генерируем фейковый booking"""
    @staticmethod
    def random_fake_booking():
        firstname = fake.user_name()
        last_name = fake.last_name()
        totalprice = random.randint(1, 200)
        depositpaid = fake.boolean()
        bookingdates = {
            'checkin': fake.date(),
            'checkout': fake.date_time()
        }
        additionalneeds = fake.color_name()

        return {
            'firstname': firstname,
            'last_name': last_name,
            'total_price': totalprice,
            'depositpaid': depositpaid,
            'bookingdates': bookingdates,
            'additionalneeds': additionalneeds
        }