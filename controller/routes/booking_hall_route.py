from flask import Blueprint

from controller.actions.booking_hall_action import book_hall,check_bookings

booking_hall_route = Blueprint('booking_hall_route', __name__)

@booking_hall_route.route('/booking/hall',methods=['POST'])
def index():
    return book_hall()

@booking_hall_route.route('/booking/hall/check',methods=['POST'])
def check():
    return check_bookings()
