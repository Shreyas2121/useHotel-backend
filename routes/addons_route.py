from flask import Blueprint

from controller.addon_controller import get_addons_data

addons_route = Blueprint('addons_route', __name__)

@addons_route.route('/booking/addon/',methods=['GET'])
def route_index():
    return get_addons_data()
