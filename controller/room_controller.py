from services import rooms_service


def create_room():
    return rooms_service.service_create_room()

def get_rooms_list():
    return rooms_service.service_get_rooms_list()
