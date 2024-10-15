from pydantic import BaseModel, RootModel, Field
from typing import List

class Booking(BaseModel):
    bookingid: int = Field(..., ge=1)  # bookingid должен быть целым числом больше или равно 1

class BookingIdList(RootModel[List[Booking]]):
    pass
