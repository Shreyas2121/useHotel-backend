from flask import jsonify, request
from typing import Any
from models.booking_hall import BookingHall
from bson import ObjectId,objectid

def service_cancel_booking(id):
    booking = BookingHall.objects().get(pk=id)
    print('test')
    print(booking)
    booking.delete()
    return booking.to_json()

def service_get_bookings_by_email(email):

    bookings = BookingHall.objects().filter(booking_useremail=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings))