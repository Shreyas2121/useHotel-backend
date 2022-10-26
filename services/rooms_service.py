from flask import jsonify
from models.Room import Room


def service_get_rooms_list():
    rooms = Room.objects()  # type: ignore
    return jsonify({'rooms': [room.to_json() for room in rooms]})