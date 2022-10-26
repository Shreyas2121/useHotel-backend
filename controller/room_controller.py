from services import rooms_service

def get_rooms_list():
    return rooms_service.service_get_rooms_list()