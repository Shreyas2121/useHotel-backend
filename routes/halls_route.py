from flask import Blueprint
from controller.hall_controller import add_hall_controller, get_halls_controller

halls_route = Blueprint('halls_route', __name__)


@halls_route.route('/hall', methods=['POST'])
def add_hall():
    return add_hall_controller()


@halls_route.route('/hall', methods=['GET'])
def get_halls():
    return get_halls_controller()
