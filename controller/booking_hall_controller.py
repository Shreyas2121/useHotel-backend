from services import booking_hall_service
from services import cancelling_hall_service

def get_hall_bookings_controller():
    return booking_hall_service.get_hall_bookings_service()

def book_hall_controller():
    return booking_hall_service.book_hall_service()

def get_halls_availability_controller():
    return booking_hall_service.check_hall_availability_service()

def delete_hall_booking_controller():
    return cancelling_hall_service.delete_booking_service()

def get_bookings_by_email_controller():
    return cancelling_hall_service.get_bookings_by_email_service()
