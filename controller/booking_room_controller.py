from services import booking_room_service
from services import cancelling_room_service

def book_room_controller():
    return booking_room_service.service_book_room()

def get_booking_rooms_controller():
    return booking_room_service.service_get_bookings()

def check_booking_room_controller():
    return booking_room_service.service_check_room_availability()


def cancel_room_booking_controller():
    return cancelling_room_service.service_cancel_booking()

def get_bookings_by_email_controller():
    return cancelling_room_service.service_get_bookings_by_email()
