from datetime import date
from typing import Any
from flask import Response, jsonify, request
from datetime import datetime
from dateutil import parser
import requests

from models.BookingRoom import BookingRoom

def book_room_service():
    data: Any = request.get_json()
    try:
        obj = BookingRoom(
        name=data['name'],
        email=data['email'],
        date=data['date'],
        check_in=data['checkin'],
        check_out=data['checkout'],
        room_type=data['category'],
        room_price=data['price'],
        no_of_rooms=data['no'],
        addOns=data['selectedAddons'],
        coupon = data['coupon'],
        special_request=data['specialReq'],
        total=data['total'],
        )
        obj.save()
    except Exception as e:
        return Response(status=400, mimetype='application/json', response=jsonify({"error": str(e)}))

    return Response(status=200, mimetype='application/json', response='{"message": "Booking Successful"}')

def get_bookings_service():
    bookings = BookingRoom.objects()
    return Response(status=200, mimetype='application/json', response=list(map(lambda x: x.to_json(), bookings)))


def check_room_availability_service():
    data: Any = request.get_json()
    checkin = data['checkIn']
    checkout = data['checkOut']
    parsed_check_in = parser.isoparse(checkin)
    parsed_check_out = parser.isoparse(checkout)

    obj = BookingRoom.objects(check_in_date__lte=parsed_check_in, check_out_date__gt=parsed_check_in,)
    obj2 = BookingRoom.objects(check_in_date__lt=parsed_check_out, check_out_date__gte=parsed_check_out,)
    data = list(map(lambda x: x.to_json(), obj))
    data1 = list(map(lambda x: x.to_json(), obj2))

    for i in data1:
        if not i in data:
            data.append(i)

    res = requests.get('http://127.0.0.1:5000/api/room/getDetails')

    available_rooms = {}
    for each in res.json().get('rooms'):
        available_rooms[each["category"]] = each["total_rooms"]

    new={}
    for i in data:
        for key,value in i.items():
            if key == 'category':
                if value in new:
                    new[value] = new[value]+i['num_of_rooms']
                else:
                    new[value] = i['num_of_rooms']

    for key, value in new.items():
        if key in available_rooms:
            available_rooms[key] -= int(value)

    return available_rooms
