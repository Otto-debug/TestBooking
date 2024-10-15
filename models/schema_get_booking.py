from pydantic import BaseModel, Field, conint, constr
from datetime import date

class BookingDates(BaseModel):
    checkin: date
    checkout: date

class Booking(BaseModel):
    firstname: constr(min_length=1)  # Имя не должно быть пустым
    lastname: constr(min_length=1)  # Фамилия не должна быть пустой
    totalprice: conint(ge=0)  # Общая цена должна быть положительным целым числом
    depositpaid: bool  # Поле с информацией об оплате депозита
    bookingdates: BookingDates  # Вложенный объект с датами
    additionalneeds: str = "None"  # Дополнительные пожелания, по умолчанию None
