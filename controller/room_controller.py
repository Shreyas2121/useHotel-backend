from services import rooms_service

def create_room_controller():
    return rooms_service.create_room_service()

def get_rooms_list_controller():
    return rooms_service.get_rooms_service()
