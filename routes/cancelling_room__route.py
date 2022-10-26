from flask import Blueprint

from controller.actions.cancelling_room_action import cancel_booking ,get_bookings_by_email

cancel_room_route = Blueprint('cancel_room_route', __name__)

@cancel_room_route.route('/reservation/room/<string:_id>',methods=['DELETE'])
def cancel(_id):
    return cancel_booking(_id)


@cancel_room_route.route('/reservation/get/room/<string:email>',methods=['GET'])
def get(email):
    print(email)
    return get_bookings_by_email(email)
