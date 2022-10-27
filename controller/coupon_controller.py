from services import coupon_service

def create_coupon_controller():
    return coupon_service.service_create_coupon()

def get_coupons():
    return coupon_service.service_get_coupons()

def validate_coupon_controller():
    return coupon_service.service_check_coupon()
