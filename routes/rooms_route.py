from flask import Blueprint
from controller.room_controller import get_rooms_list_controller, create_room_controller

rooms_bp = Blueprint('rooms_route', __name__)


@rooms_bp.route('/room/create', methods=['POST'])
def route_create_room():
    return create_room_controller()


@rooms_bp.route('/room/getDetails', methods=['GET'])
def route_index():
    return get_rooms_list_controller()
