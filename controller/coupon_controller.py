from services import coupon_service

def create_coupon_controller():
    return coupon_service.create_coupon_service()

def get_coupons_controller():
    return coupon_service.get_coupons_service()

def validate_coupon_controller():
    return coupon_service.validate_coupon_service()
