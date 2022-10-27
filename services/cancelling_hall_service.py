from typing import Any
from flask import Response
from models.BookingHall import BookingHall

def delete_booking_service(id):
    booking = BookingHall.objects().get(pk=id)
    booking.delete()
    return Response("Hall Booking Deleted", status=200, mimetype='application/json')

def get_bookings_by_email_service(email):
    bookings = BookingHall.objects().filter(email=email)
    print(bookings)
    return Response(list(map(lambda x: x.to_json(), bookings)), status=200, mimetype='application/json')
