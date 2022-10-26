from flask import Blueprint

from controller.reviews_controller import get_reviews, add_reviews, get_top_reviews

reviews_route = Blueprint('reviews_route', __name__)


@reviews_route.route('/reviews/',methods=['GET'])
def route_get():
    return get_reviews()

@reviews_route.route('/reviews/',methods=['POST'])
def route_add():
    return add_reviews()

@reviews_route.route('/reviews/featured',methods=['GET'])
def route_featured():
    return get_top_reviews()

