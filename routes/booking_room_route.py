from flask import Blueprint

from controller.booking_room_controller import book_room,get_booking_rooms,check_booking_room
booking_route = Blueprint('booking_route', __name__)

@booking_route.route('/booking/room', methods=['POST'])
def route_book():
    return book_room()

@booking_route.route('/booking/room/get', methods=['GET'])
def route_get():
    return get_booking_rooms()

@booking_route.route('/booking/room/check', methods=['POST'])
def route_check():
    return check_booking_room()
