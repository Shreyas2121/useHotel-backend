from services import booking_hall_service
from services import cancelling_hall_service


def book_hall_controller():
    return booking_hall_service.service_book_hall()

def get_halls_availability_controller():
    return booking_hall_service.service_check_hall_availability()

def delete_hall_booking_controller():
    return cancelling_hall_service.delete_booking_service()

def get_bookings_by_email_controller():
    return cancelling_hall_service.get_bookings_by_email_service()