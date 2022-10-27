from flask import Blueprint

from controller.booking_hall_controller import book_hall_controller,get_halls_availability_controller

booking_hall_route = Blueprint('booking_hall_route', __name__)

@booking_hall_route.route('/booking/hall',methods=['POST'])
def book_hall():
    return book_hall_controller()

@booking_hall_route.route('/booking/hall/availability',methods=['POST'])
def get_halls_availability():
    return get_halls_availability_controller()
