from flask import Blueprint

from controller.actions.cancelling_hall_action import cancel_booking ,get_bookings_by_email

cancel_hall_route = Blueprint('cancel_hall_route', __name__)

@cancel_hall_route.route('/reservation/hall/<string:_id>',methods=['DELETE'])
def cancel(_id):
    return cancel_booking(_id)


@cancel_hall_route.route('/reservation/get/hall/<string:email>',methods=['GET'])
def get(email):
    print(email)
    return get_bookings_by_email(email)
