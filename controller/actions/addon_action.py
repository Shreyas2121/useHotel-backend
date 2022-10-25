
from models.add_on import AddOns

def get_addons_data():
    addonObj = AddOns.objects()
    return  list(map(lambda x: x.to_json(), addonObj))[0]
