# from pydantic import BaseModel
# from typing import Optional
# from datetime import date
#
# class BookingDates(BaseModel):
#     checkin: date
#     checkout: date
#
# class Booking(BaseModel):
#     firstname: str
#     lastname: str
#     totalprice: int
#     depositpaid: bool
#     bookingdates: BookingDates
#     additionalneeds: Optional[str] = None
#
# class BookingResponse(BaseModel):
#     bookingid: int
#     booking: Booking
from pydantic import BaseModel, Field, conint, constr
from datetime import date

class BookingDates(BaseModel):
    checkin: date
    checkout: date

class Booking(BaseModel):
    firstname: constr(min_length=1)  # Имя должно быть строкой и не пустым
    lastname: constr(min_length=1)  # Фамилия не должна быть пустой
    totalprice: conint(ge=0)  # Общая цена - положительное целое число
    depositpaid: bool  # Логическое значение для оплаты депозита
    bookingdates: BookingDates  # Модель для дат бронирования
    additionalneeds: str = "None"  # Дополнительные пожелания, по умолчанию None

class BookingData(BaseModel):
    bookingid: conint(ge=1)  # ID бронирования должно быть целым числом >= 1
    booking: Booking  # Вложенная модель Booking
