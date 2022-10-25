from flask import jsonify, request
from typing import Any
from models.booking_room import BookingRoom
from bson import ObjectId,objectid

def cancel_booking(id):
    booking = BookingRoom.objects().get(pk=id)
    print('test')
    print(booking)
    booking.delete()
    return booking.to_json()

def get_bookings_by_email(email):

    bookings = BookingRoom.objects().filter(booking_useremail=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings))
