from flask import Blueprint

from controller.coupon_controller import create_coupon, get_coupons, check_coupon


coupons_route = Blueprint('coupons_route', __name__)


@coupons_route.route('/coupons/create', methods=['POST'])
def route_create_coupon():
    return create_coupon()

@coupons_route.route('/booking/coupon/get',methods=['GET'])
def route_get():
    return get_coupons()

@coupons_route.route('/booking/coupon',methods=['POST'])
def route_check():
    return check_coupon()
