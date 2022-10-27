from services import rooms_service

def create_room_controller():
    return rooms_service.service_create_room()

def get_rooms_list_controller():
    return rooms_service.service_get_rooms_list()
