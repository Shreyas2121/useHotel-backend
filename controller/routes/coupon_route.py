from flask import Blueprint
from controller.actions.coupon_action import get_coupons,check_coupon


coupons_route = Blueprint('coupons_route', __name__)

@coupons_route.route('/booking/coupon/get',methods=['GET'])
def get():
    return get_coupons()

@coupons_route.route('/booking/coupon',methods=['POST'])
def post():
    return check_coupon()
