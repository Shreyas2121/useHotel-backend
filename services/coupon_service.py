from flask import Response, jsonify, request
from models.Coupon import Coupon


def create_coupon_service():
    coupon_code = request.get_json()['coupon_code']
    discount_res = request.get_json()['discount']
    coupon = Coupon(code=coupon_code, discount_percentage=discount_res)
    coupon.save()
    return Response(status=200, mimetype='application/json', response='{"message": "Coupon Created"}')

def get_coupons_service():
    couponObj = Coupon.objects()
    return Response(status=200, mimetype='application/json', response=jsonify({'coupons': [coupon.to_json() for coupon in couponObj]}))


def check_coupon_service():
    coupon_res = request.get_json()['coupon']
    couponObj = Coupon.objects(code=coupon_res)
    if couponObj:
        return Response(status=200, mimetype='application/json', response=jsonify(couponObj[0].discount_percentage))
    else:
        return Response(status=400, mimetype='application/json', response={"message": "Invalid Coupon"})
