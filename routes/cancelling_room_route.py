from flask import Blueprint

from controller.booking_room_controller import cancel_room_booking, delete_room_booking, get_bookings_by_email
cancel_room_route = Blueprint('cancel_room_route', __name__)

@cancel_room_route.route('/booking/room/<string:_id>',methods=['DELETE'])
def route_cancel(_id):
    return delete_room_booking(_id)

@cancel_room_route.route('/booking/get/room/<string:email>',methods=['GET'])
def route_get(email):
    print(email)
    return get_bookings_by_email(email)
