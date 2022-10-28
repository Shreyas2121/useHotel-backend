from services import addon_service


def create_addons_controller():
    return addon_service.create_addon_service()


def get_addons_controller():
    return addon_service.get_addons_service()
