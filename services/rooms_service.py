from typing import Any
from flask import jsonify,request
from models.Room import Room

def create_room_service():
    data:Any = request.get_json()
    room = Room(
        category = data['category'],
        price = data['price'],
        occupancy = data['occupancy'],
        desc = data['desc'],
        amenities = data['amenities'],
        images = data['images'],
        total_rooms = data['total_rooms'],
        area_sq_ft = data['area_sq_ft']
    )
    room.save()
    return jsonify({'room': room.to_json()})


def get_rooms_service():
    rooms = Room.objects()  # type: ignore
    return jsonify({'rooms': [room.to_json() for room in rooms]}), 200
