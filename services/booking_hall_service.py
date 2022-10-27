from typing import Any
from flask import jsonify, request
from dateutil import parser
import requests

from models.BookingHall import BookingHall

def service_book_hall():
    data : Any = request.get_json()
    BookingHall(
        name = data['name'],
        email = data['email'],
        date = data['date'],
        check_in = data['checkin'],
        check_out=data['checkout'],
        hall_type = data['category'],
        hall_price = data['price'],
        addOns = data['selectedAddons'],
        coupon = data['coupon'],
        special_request = data['specialReq'],
        total = data['total'],
    ).save()
    return jsonify({"message":"Booking Successful"})

# def check_bookings():
#     checkin = request.get_json()['checkin']
#     parsed_check_in = parser.isoparse(checkin)
#     bookings = BookingHall.objects(check_in=parsed_check_in)
#     return list(map(lambda x: x.hall_type, bookings))

def service_check_bookings():
    data: Any = request.get_json()
    checkin = data['checkIn']
    checkout = data['checkOut']
    parsed_check_in = parser.isoparse(checkin)
    parsed_check_out = parser.isoparse(checkout)

    obj1 = BookingHall.objects(check_in__lte=parsed_check_in, check_out__gte=parsed_check_in,)
    obj2 = BookingHall.objects(check_in__lte=parsed_check_out, check_out__gte=parsed_check_out,)
    data1 = list(map(lambda x: x.to_json(), obj1))
    data2 = list(map(lambda x: x.to_json(), obj2))

    data=data1+data2

    res = requests.get('http://usehotelbackend-env.eba-x3zhkiev.ap-northeast-1.elasticbeanstalk.com/booking/hall/getDetails')

    available_halls = {}
    for each in res.json().get('halls'):
        available_halls[each["category"]] = each["total_halls"]

    new={}
    for i in data:
        for key,value in i.items():
            if key == 'category':
                if value in new:
                    new[value] +=  1
                else:
                    new[value] = 1

    for key, value in new.items():
        if key in available_halls:
            available_halls[key] -= int(value)

    return available_halls
