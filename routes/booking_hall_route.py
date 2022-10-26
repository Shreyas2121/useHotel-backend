from flask import Blueprint

from controller.booking_hall_controller import book_hall,check_booking_hall

booking_hall_route = Blueprint('booking_hall_route', __name__)

@booking_hall_route.route('/booking/hall',methods=['POST'])
def route_index():
    return book_hall()

@booking_hall_route.route('/booking/hall/check',methods=['POST'])
def route_check():
    return check_booking_hall()
