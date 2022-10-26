from services import hall_service

def create_hall():
    return hall_service.service_create_hall()

def get_halls():
    return hall_service.service_get_halls()

