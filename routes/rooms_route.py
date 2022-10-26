from flask import Blueprint
from controller.room_controller import get_rooms_list,create_room
rooms_route = Blueprint('rooms_route', __name__)


@rooms_route.route('/room/create', methods=['POST'])
def route_create_room():
    return create_room()

@rooms_route.route('/booking/room/getDetails',methods=['GET'])
def route_index():
    return get_rooms_list()
