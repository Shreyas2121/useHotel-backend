from flask import Response, jsonify
from models.BookingRoom import BookingRoom

def delete_booking_service(id):
    booking = BookingRoom.objects().get(pk=id)
    print('test')
    print(booking)
    booking.delete()
    return jsonify({"message":"Room Booking Deleted"}),200

def get_bookings_by_email_service(email):
    bookings = BookingRoom.objects().filter(email=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings)),200
