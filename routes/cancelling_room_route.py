from flask import Blueprint
from controller.booking_hall_controller import get_bookings_by_email_controller

from controller.booking_room_controller import  delete_room_booking_controller, get_bookings_by_email_controller
cancel_room_route = Blueprint('cancel_room_route', __name__)

@cancel_room_route.route('/booking/room/<string:_id>',methods=['DELETE'])
def route_cancel(_id):
    return delete_room_booking_controller(_id)

@cancel_room_route.route('/booking/get/room/<string:email>',methods=['GET'])
def route_get(email):
    print(email)
    return get_bookings_by_email_controller(email)
