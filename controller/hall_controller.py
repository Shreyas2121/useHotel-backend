from services import hall_service

def add_hall_controller():
    return hall_service.add_hall_service()

def get_halls_controller():
    return hall_service.get_halls_service()
