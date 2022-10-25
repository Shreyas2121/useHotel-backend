from datetime import date
from typing import Any
from flask import jsonify, request
from dateutil import parser
import requests

from models.booking_hall import BookingHall

def book_hall():
    data : Any = request.get_json()
    BookingHall(
        booking_username = data['name'],
        booking_useremail = data['email'],
        booking_date = data['date'],
        booking_check_in = data['checkin'],
        booking_check_out=data['checkout'],
        booking_hall_type = data['roomType'],
        booking_hall_price = data['roomPrice'],
        booking_addOns = data['selectedAddons'],
        booking_coupon_id = data['couponId'],
        booking_coupon_discount = data['discount'],
        booking_special_request = data['specialReq'],
        booking_total = data['total'],
    ).save()
    return jsonify({"message":"Booking Successful"})

# def check_bookings():
#     checkin = request.get_json()['checkin']
#     parsed_check_in = parser.isoparse(checkin)
#     bookings = BookingHall.objects(booking_check_in=parsed_check_in)
#     return list(map(lambda x: x.booking_hall_type, bookings))

def check_bookings():
    data: Any = request.get_json()
    checkin = data['checkIn']
    checkout = data['checkOut']
    parsed_check_in = parser.isoparse(checkin)
    parsed_check_out = parser.isoparse(checkout)

    booking_obj1 = BookingHall.objects(booking_check_in__lte=parsed_check_in, booking_check_out__gte=parsed_check_in,)
    booking_obj2 = BookingHall.objects(booking_check_in__lte=parsed_check_out, booking_check_out__gte=parsed_check_out,)
    booking_data1 = list(map(lambda x: x.to_json(), booking_obj1))
    booking_data2 = list(map(lambda x: x.to_json(), booking_obj2))

    booking_data=booking_data1+booking_data2

    res = requests.get('http://127.0.0.1:5000/booking/hall/getDetails')

    available_halls = {}
    for each in res.json().get('halls'):
        available_halls[each["hall_type"]] = each["total_halls"]

    new={}
    for i in booking_data:
        for key,value in i.items():
            if key == 'booking_hall_type':
                if value in new:
                    new[value] +=  1
                else:
                    new[value] = 1

    for key, value in new.items():
        if key in available_halls:
            available_halls[key] -= int(value)

    return available_halls