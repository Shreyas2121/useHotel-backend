from typing import Any
from flask import Response, jsonify,request
from models.Hall import Hall

def add_hall_service():
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
    return Response(status=200, mimetype='application/json', response='{"message": "Added Successfully"}')


def get_halls_service():
    all_halls = Hall.objects()
    return jsonify({'halls': [hall.to_json() for hall in all_halls]}), 200
