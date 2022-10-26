from services import coupon_service

def create_coupon():
    return coupon_service.service_create_coupon()

def get_coupons():
    return coupon_service.service_get_coupons()

def check_coupon():
    return coupon_service.service_check_coupon()
