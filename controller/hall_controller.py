from services import hall_service

def add_hall_controller():
    return hall_service.service_add_hall()

def get_halls_controller():
    return hall_service.service_get_halls()