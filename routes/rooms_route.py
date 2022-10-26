from flask import Blueprint
from controller.actions.rooms_action import get_rooms_list

rooms_route = Blueprint('rooms_route', __name__)


@rooms_route.route('/booking/room/getDetails',methods=['GET'])
def index():
    return get_rooms_list()
