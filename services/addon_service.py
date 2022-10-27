from models.AddOn import AddOns
from flask import request


def create_addon_service():
    name = request.json['name']
    price = request.json['price']
    addonObj = AddOns(name=name, price=price)
    addonObj.save()
    return addonObj.to_json()

def get_addons_data_service():
    addonObj = AddOns .objects()
    return  list(map(lambda x: x.to_json(), addonObj))
