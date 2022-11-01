from flask import Blueprint

from controller.coupon_controller import create_coupon_controller, get_coupons_controller, validate_coupon_controller

coupons_bp = Blueprint('coupons_route', __name__)


@coupons_bp.route('/coupons', methods=['POST'])
def create_coupon():
    return create_coupon_controller()


@coupons_bp.route('/coupons', methods=['GET'])
def route_get():
    return get_coupons_controller()


@coupons_bp.route('/coupon/validate', methods=['POST'])
def route_check():
    return validate_coupon_controller()
