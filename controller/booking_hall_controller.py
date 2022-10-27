from services import booking_hall_service
from services import cancelling_hall_service


def book_hall():
    return booking_hall_service.service_book_hall()

def check_booking_hall():
    return booking_hall_service.service_check_bookings()

def cancel_hall_booking():
    return cancelling_hall_service.service_cancel_booking()

def get_bookings_by_email():
    return cancelling_hall_service.service_get_bookings_by_email()