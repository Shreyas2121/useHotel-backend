from models.addon import Addon

def service_get_addons_data():
    addonObj = AddOns.objects()
    return  list(map(lambda x: x.to_json(), addonObj))[0]
