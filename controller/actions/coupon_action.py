from flask import jsonify, request
from models.coupon import Coupon


def get_coupons():
    couponObj = Coupon.objects()
    return jsonify({'coupons': [coupon.to_json() for coupon in couponObj]})


def check_coupon():
    coupon_res = request.get_json()['coupon']

    for coupan in Coupon.objects():
        try:
            if coupan.coupons[coupon_res]:
                return str(coupan.coupons[coupon_res])
        except:
            return("Invalid Coupon")
    return "Invalid Coupon"
