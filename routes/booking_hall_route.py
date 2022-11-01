from flask import Blueprint, request

from controller.booking_hall_controller import get_hall_bookings_controller, book_hall_controller, get_hall_availability_controller, delete_hall_booking_controller, get_bookings_by_email_controller

hall_booking_bp = Blueprint('booking_hall_route', __name__)


@hall_booking_bp.route('/booking/hall', methods=['GET'])
def get_hall_bookings():
    return get_hall_bookings_controller()


@hall_booking_bp.route('/booking/hall', methods=['POST'])
def book_hall():
    return book_hall_controller()


@hall_booking_bp.route('/booking/hall/availability', methods=['GET'])
def get_halls_availability():
    return get_hall_availability_controller()


@hall_booking_bp.route('/booking/hall/<string:_id>', methods=['DELETE'])
def delete_hall_booking(_id):
    return delete_hall_booking_controller(_id)


@hall_booking_bp.route('/booking/hall/<string:email>', methods=['GET'])
def get_hall_bookings_by_email(email):
    print(email)
    return get_bookings_by_email_controller(email)
