from models.AddOn import AddOns
from flask import request


def service_create_addon():
    name = request.json['name']
    price = request.json['price']
    addonObj = AddOns(name=name, price=price)
    addonObj.save()
    return addonObj.to_json()

def service_get_addons_data():
    addonObj = AddOns .objects()
    return  list(map(lambda x: x.to_json(), addonObj))
