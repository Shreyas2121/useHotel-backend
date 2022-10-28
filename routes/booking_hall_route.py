from flask import Blueprint, request

from controller.booking_hall_controller import get_hall_bookings_controller, book_hall_controller, \
    get_halls_availability_controller

booking_hall_route = Blueprint('booking_hall_route', __name__)


@booking_hall_route.route('/booking/hall', methods=['GET'])
def get_hall_bookings():
    return get_hall_bookings_controller()


@booking_hall_route.route('/booking/hall', methods=['POST'])
def book_hall():
    return book_hall_controller()


@booking_hall_route.route('/booking/hall/availability', methods=['GET'])
def get_halls_availability():
    return get_halls_availability_controller()
