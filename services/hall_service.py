from typing import Any
from flask import jsonify,request
from models.Hall import Hall

def service_add_hall():
    data:Any = request.get_json()
    hall = Hall(
        category = data['category'],
        price = data['price'],
        max_guests = data['max_guests'],
        desc = data['desc'],
        amenities = data['amenities'],
        images = data['images'],
    )
    hall.save()
    return jsonify({'hall': hall.to_json()})


def service_get_halls():
    all_halls = Hall.objects()
    return map(lambda x: x.to_json(), all_halls)