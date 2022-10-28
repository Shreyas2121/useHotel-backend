from flask import Blueprint

from controller.booking_room_controller import book_room_controller, get_room_bookings_controller, get_room_availability_controller, delete_room_booking_controller, get_bookings_by_email_controller

booking_route = Blueprint('booking_route', __name__)


@booking_route.route('/booking/room', methods=['POST'])
def book_room():
    return book_room_controller()


@booking_route.route('/booking/room', methods=['GET'])
def get_rooms():
    return get_room_bookings_controller()


@booking_route.route('/booking/room/availability', methods=['POST'])
def get_rooms_availability():
    return get_room_availability_controller()


@booking_route.route('/booking/room/<string:_id>', methods=['DELETE'])
def delete_room_booking(_id):
    return delete_room_booking_controller(_id)


@booking_route.route('/booking/room/<string:email>', methods=['GET'])
def get_room_bookings_by_email(email):
    print(email)
    return get_bookings_by_email_controller(email)
