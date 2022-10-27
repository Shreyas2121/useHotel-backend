from flask import Blueprint

from controller.booking_room_controller import book_room_controller,get_booking_rooms_controller,check_booking_room_controller
booking_route = Blueprint('booking_route', __name__)

@booking_route.route('/booking/room', methods=['POST'])
def book_room():
    return book_room_controller()

@booking_route.route('/booking/room', methods=['GET'])
def route_get():
    return get_booking_rooms_controller()

@booking_route.route('/booking/room/check', methods=['POST'])
def route_check():
    return check_booking_room_controller()
