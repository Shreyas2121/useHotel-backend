from typing import Any
from models.BookingHall import BookingHall

def service_cancel_booking(id):
    booking = BookingHall.objects().get(pk=id)
    booking.delete()
    return booking.to_json()

def service_get_bookings_by_email(email):

    bookings = BookingHall.objects().filter(booking_useremail=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings))
