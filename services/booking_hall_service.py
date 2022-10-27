from typing import Any
from flask import Response, jsonify, request
from dateutil import parser
import requests

from models.BookingHall import BookingHall

def service_book_hall():
    data: Any = request.get_json()

    try:
        obj = BookingHall(
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
        )
        obj.save()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return Response(status=200, mimetype='application/json', response='{"message": "Booking Successful"}')

def service_check_hall_availability():
    data: Any = request.get_json()
    # checkin = data['checkIn']
    # checkout = data['checkOut']
    parsed_check_in = parser.isoparse(data['checkIn'])
    parsed_check_out = parser.isoparse(data['checkOut'])

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
