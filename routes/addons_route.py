from flask import Blueprint

from controller.addon_controller import get_addons_controller, create_addons_controller

addons_bp = Blueprint('addons_route', __name__)


@addons_bp.route('/addon', methods=['POST'])
def create_addon():
    return create_addons_controller()


@addons_bp.route('/addon', methods=['GET'])
def get_addons():
    return get_addons_controller()
