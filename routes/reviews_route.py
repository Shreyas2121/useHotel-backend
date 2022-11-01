from flask import Blueprint

from controller.reviews_controller import get_reviews_controller, get_top_reviews_controller, add_review_controller

reviews_bp = Blueprint('reviews_route', __name__)


@reviews_bp.route('/reviews', methods=['GET'])
def get_reviews_route():
    return get_reviews_controller()


@reviews_bp.route('/reviews', methods=['POST'])
def add_review_route():
    return add_review_controller()


@reviews_bp.route('/reviews/featured', methods=['GET'])
def get_featured_reviews_route():
    return get_top_reviews_controller()
