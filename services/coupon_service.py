from flask import Response, jsonify, request
from models.Coupon import Coupon


def create_coupon_service():
    coupon_code = request.get_json()['coupon_code']
    discount_res = request.get_json()['discount']
    coupon = Coupon(code=coupon_code, discount_percentage=discount_res)
    coupon.save()
    return jsonify({'message': 'Coupon Created'}), 200
def get_coupons_service():
    couponObj = Coupon.objects()
    return jsonify({'coupons': [coupon.to_json() for coupon in couponObj]}), 200


def check_coupon_service():
    print(request.get_json())
    coupon_res = request.get_json()['coupon']
    couponObj = Coupon.objects(code=coupon_res)
    if couponObj:
        return jsonify(couponObj[0].discount_percentage), 200
    else:
        return "Invalid Coupon", 400
