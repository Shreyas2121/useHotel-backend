from flask import jsonify, request,Blueprint
from models.hall import Hall

from controller.actions.hall_action import get_halls,create_hall

halls_route = Blueprint('halls_route', __name__)


@halls_route.route('/booking/hall/post',methods=['GET'])
def post():
    return create_hall()


@halls_route.route('/booking/hall/getDetails',methods=['GET'])
def get():
    return get_halls()
