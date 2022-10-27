from typing import Any
from flask import Response, jsonify, request
from dateutil import parser
import requests

from models.BookingHall import BookingHall
from services.hall_service import get_halls_service

def get_hall_bookings_service():
    booked_halls = BookingHall.objects()
    return Response(status=200, mimetype='application/json', response=map(lambda x: x.to_json(), booked_halls))


def book_hall_service():
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

def check_hall_availability_service():
    data: Any = request.get_json()
    # print(data)
    # checkin = data['checkIn']
    # checkout = data['checkOut']
    # parsed_check_in = parser.isoparse(data['checkIn'])
    # parsed_check_out = parser.isoparse(data['checkOut'])

    # obj1 = BookingHall.objects(check_in__lte=parser.isoparse(data['checkIn']), check_out__gte=parser.isoparse(data['checkIn']),)
    # obj2 = BookingHall.objects(check_in__lte=parser.isoparse(data['checkOut']), check_out__gte=parser.isoparse(data['checkOut']),)

    booked_halls_checkin = BookingHall.objects(check_in_date__lte=parser.isoparse(data['checkIn']), check_out_date__gte=parser.isoparse(data['checkIn']),)
    booked_hall_checkout = BookingHall.objects(check_in_date__lte=parser.isoparse(data['checkOut']), check_out_date__gte=parser.isoparse(data['checkOut']),)

    # data1 = list(map(lambda x: x.to_json(), booked_halls_checkin))
    # data2 = list(map(lambda x: x.to_json(), booked_hall_checkout))

    # data=data1+data2

    hall_inventory = get_halls_service()

    booked_halls=(list(map(lambda x: x.to_json(), booked_halls_checkin)))+(list(map(lambda x: x.to_json(), booked_hall_checkout)))

    # hall_inventory = get_halls_service()

    # print(res[0])
    # print(hall_inventory)

    available_halls = {}
    for each in hall_inventory[0].json.get('halls'):
        available_halls[each["category"]] = each["total_halls"]

    # print(available_halls)

    new={}
    for i in booked_halls:
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