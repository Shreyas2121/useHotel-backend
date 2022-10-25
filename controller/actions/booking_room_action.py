from datetime import date
from typing import Any
from flask import jsonify, request
from datetime import datetime
from dateutil import parser
import requests

from models.booking_room import BookingRoom


def book_room():
    data: Any = request.get_json()
    print(data)

    try:
        booking_obj = BookingRoom(
        booking_username=data['name'],
        booking_useremail=data['email'],
        booking_date=data['date'],
        booking_check_in=data['checkin'],
        booking_check_out=data['checkout'],
        booking_room_type=data['roomType'],
        booking_room_price=data['roomPrice'],
        booking_no_of_rooms=data['no'],
        booking_addOns=data['selectedAddons'],
        booking_coupon_id=data['couponId'],
        booking_coupon_discount=data['discount'],
        booking_special_request=data['specialReq'],
        booking_total=data['total'],
        )
        booking_obj.save()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "Booking Successful",})

def get_bookings():
    bookings = BookingRoom.objects()
    return list(map(lambda x: x.to_json(), bookings))


def check_booking():
    data: Any = request.get_json()
    checkin = data['checkIn']
    checkout = data['checkOut']
    parsed_check_in = parser.isoparse(checkin)
    parsed_check_out = parser.isoparse(checkout)

    booking_obj = BookingRoom.objects(booking_check_in__lte=parsed_check_in, booking_check_out__gt=parsed_check_in,)
    booking_obj2 = BookingRoom.objects(booking_check_in__lt=parsed_check_out, booking_check_out__gte=parsed_check_out,)
    booking_data = list(map(lambda x: x.to_json(), booking_obj))
    booking_data1 = list(map(lambda x: x.to_json(), booking_obj2))

    for i in booking_data1:
        if not i in booking_data:
            booking_data.append(i)

    res = requests.get('http://127.0.0.1:5000/booking/room/getDetails')

    available_rooms = {}
    for each in res.json().get('rooms'):
        available_rooms[each["room_type"]] = each["total_rooms"]

    new={}
    for i in booking_data:
        for key,value in i.items():
            if key == 'booking_room_type':
                if value in new:
                    new[value] = new[value]+i['booking_no_of_rooms']
                else:
                    new[value] = i['booking_no_of_rooms']

    for key, value in new.items():
        if key in available_rooms:
            available_rooms[key] -= int(value)

    return available_rooms
