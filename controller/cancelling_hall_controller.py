from services import cancelling_hall_service

def cancel_hall_booking():
    return cancelling_hall_service.service_cancel_booking()

def get_bookings_by_email():
    return cancelling_hall_service.service_get_bookings_by_email()

