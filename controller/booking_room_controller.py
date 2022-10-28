from services import booking_room_service

def book_room_controller():
    return booking_room_service.book_room_service()

def get_booking_rooms_controller():
    return booking_room_service.get_bookings_service()

def get_booking_room_controller():
    return booking_room_service.get_room_availability_service()

def delete_room_booking_controller(_id):
    return booking_room_service.delete_booking_service(_id)

def get_bookings_by_email_controller(email):
    return booking_room_service.get_bookings_by_email_service(email)
