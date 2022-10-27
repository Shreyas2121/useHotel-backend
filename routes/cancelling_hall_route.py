from flask import Blueprint

from controller.booking_hall_controller import cancel_hall_booking, get_bookings_by_email

cancel_hall_route = Blueprint('cancel_hall_route', __name__)

@cancel_hall_route.route('/reservation/hall/<string:_id>',methods=['DELETE'])
def route_cancel(_id):
    return cancel_hall_booking(_id)

@cancel_hall_route.route('/reservation/get/hall/<string:email>',methods=['GET'])
def route_get(email):
    print(email)
    return get_bookings_by_email(email)
