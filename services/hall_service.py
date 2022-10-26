from typing import Any
from flask import jsonify,request
from models.Hall import Hall

def service_create_hall():
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
    halls = Hall.objects()
    return jsonify({'halls': [hall.to_json() for hall in halls]})
