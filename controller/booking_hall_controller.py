from services import booking_hall_service
from services import cancelling_hall_service

def get_hall_bookings_controller():
    return booking_hall_service.service_get_hall_bookings()

def book_hall_controller():
    return booking_hall_service.service_book_hall()

def get_halls_availability_controller():
    return booking_hall_service.service_check_hall_availability()

def cancel_hall_booking_controller():
    return cancelling_hall_service.service_cancel_booking()

def get_bookings_by_email_controller():
    return cancelling_hall_service.service_get_bookings_by_email()