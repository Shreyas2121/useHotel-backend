from flask import Response
from models.BookingRoom import BookingRoom

def service_delete_booking(id):
    booking = BookingRoom.objects().get(pk=id)
    print('test')
    print(booking)
    booking.delete()
    return Response("Hall Booking Deleted", status=200, mimetype='application/json')

def service_get_bookings_by_email(email):

    bookings = BookingRoom.objects().filter(email=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings))
