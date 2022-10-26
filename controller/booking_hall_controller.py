from services import booking_hall_service

def book_hall():
    return booking_hall_service.service_book_hall()

def check_booking_hall():
    return booking_hall_service.service_check_bookings()