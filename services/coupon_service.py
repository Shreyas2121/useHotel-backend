from flask import Response, jsonify, request
from models.Coupon import Coupon


def service_create_coupon():
    coupon_code = request.get_json()['coupon_code']
    discount_res = request.get_json()['discount']
    coupon = Coupon(code=coupon_code, discount_percentage=discount_res)
    coupon.save()
    # return jsonify({'coupon': coupon.to_json()})
    return Response(status=200, mimetype='application/json', response='{"message": "Coupon Created"}')

def service_get_coupons():
    couponObj = Coupon.objects()
    return jsonify({'coupons': [coupon.to_json() for coupon in couponObj]})


def service_check_coupon():
    coupon_res = request.get_json()['coupon']
    couponObj = Coupon.objects(code=coupon_res)
    if couponObj:
        return Response(status=200, mimetype='application/json', response=jsonify(couponObj[0].discount_percentage))
    else:
        return Response(status=400, mimetype='application/json', response={"message": "Invalid Coupon"})
