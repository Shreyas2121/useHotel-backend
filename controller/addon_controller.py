from services import addon_service

def create_addons_controller():
    return addon_service.service_create_addon()

def get_addons_controller():
    return addon_service.service_get_addons_data()


