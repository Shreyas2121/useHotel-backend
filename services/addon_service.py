from models.add_on import AddOns
def service_get_addons_data():
    addonObj = AddOns.objects()
    return  list(map(lambda x: x.to_json(), addonObj))[0]
