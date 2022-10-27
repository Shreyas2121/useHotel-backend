from typing import Any
from flask import Response
from models.BookingHall import BookingHall

def service_delete_booking(id):
    booking = BookingHall.objects().get(pk=id)
    booking.delete()
    return Response("Hall Booking Deleted", status=200, mimetype='application/json')

def service_get_bookings_by_email(email):
    bookings = BookingHall.objects().filter(email=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings))
