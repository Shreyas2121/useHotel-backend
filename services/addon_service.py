from models.AddOn import AddOns
from flask import Response, request


def create_addon_service():
    name = request.json['name']
    price = request.json['price']
    addonObj = AddOns(name=name, price=price)
    addonObj.save()
    return Response("Addon created", 201, mimetype='application/json')


def get_addons_service():
    addonObj = AddOns.objects()
    return list(map(lambda x: x.to_json(), addonObj))
