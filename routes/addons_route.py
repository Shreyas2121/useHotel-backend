from flask import Blueprint


from controller.actions.addon_action import get_addons_data

addons_route = Blueprint('addons_route', __name__)

@addons_route.route('/booking/addon/',methods=['GET'])
def index():
    return get_addons_data()
