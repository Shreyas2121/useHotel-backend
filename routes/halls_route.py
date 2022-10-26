from flask import Blueprint
from controller.hall_controller import create_hall, get_halls

halls_route = Blueprint('halls_route', __name__)


@halls_route.route('/booking/hall/post',methods=['GET'])
def route_post():
    return create_hall()

@halls_route.route('/booking/hall/getDetails',methods=['GET'])
def route_get():
    return get_halls()
