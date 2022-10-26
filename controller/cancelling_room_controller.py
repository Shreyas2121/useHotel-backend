from services import cancelling_room_service

def cancel_room_booking():
    return cancelling_room_service.service_cancel_booking()

def get_bookings_by_email():
    return cancelling_room_service.service_get_bookings_by_email()
    