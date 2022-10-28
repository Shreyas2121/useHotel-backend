from flask import Blueprint

from controller.addon_controller import get_addons_controller, create_addons_controller

addons_route = Blueprint('addons_route', __name__)


@addons_route.route('/addon', methods=['POST'])
def create_addon():
    return create_addons_controller()


@addons_route.route('/addon', methods=['GET'])
def get_addons():
    return get_addons_controller()
