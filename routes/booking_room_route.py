from flask import Blueprint

from controller.actions.booking_room_action import book_room,get_bookings,check_booking

booking_route = Blueprint('booking_route', __name__)

@booking_route.route('/booking/room', methods=['POST'])
def book():
    return book_room()


@booking_route.route('/booking/room/get', methods=['GET'])
def get():
    return get_bookings()

@booking_route.route('/booking/room/check', methods=['POST'])
def check():
    return check_booking()
