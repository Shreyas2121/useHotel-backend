from typing import Any
from flask import Response, jsonify, request
from dateutil import parser

from models.BookingHall import BookingHall
from services.hall_service import get_halls_service


def get_hall_bookings_service():
    booked_halls = BookingHall.objects()
    return Response(status=200, mimetype='application/json', response=map(lambda x: x.to_json(), booked_halls))


def book_hall_service():
    data: Any = request.get_json()
    try:
        obj = BookingHall(
            name=data['name'],
            email=data['email'],
            date=data['date'],
            check_in_date=data['checkin'],
            check_out_date=data['checkout'],
            category=data['category'],
            price=data['basePrice'],
            add_ons=data['selectedAddons'],
            coupon=data['coupon'],
            special_request=data['specialReq'],
            total=data['total'],
        )
        obj.save()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "Booking Successful"}), 200


def get_hall_availability_service():
    data: Any = request.args.to_dict()

    booked_halls_checkin = (list(map(lambda x: x.to_json(),
                                     BookingHall.objects(check_in_date__lte=parser.isoparse(data['checkIn']),
                                                         check_out_date__gte=parser.isoparse(data['checkIn']), ))))
    booked_halls_checkout = (list(map(lambda x: x.to_json(),
                                      BookingHall.objects(check_in_date__lte=parser.isoparse(data['checkOut']),
                                                          check_out_date__gte=parser.isoparse(data['checkOut']), ))))

    booked_halls_between = (list(map(lambda x: x.to_json(),
                                     BookingHall.objects(check_in_date__gte=parser.isoparse(data['checkIn']),
                                                         check_out_date__lte=parser.isoparse(data['checkOut']), ))))

    booked_halls_data = booked_halls_checkin
    booked_halls_data.extend(halls for halls in booked_halls_checkout if halls not in booked_halls_data)
    booked_halls_data.extend(halls for halls in booked_halls_between if halls not in booked_halls_data)

    hall_inventory = get_halls_service()

    total_halls_inventory = {}
    for each in hall_inventory[0].json.get('halls'):
        total_halls_inventory[each["category"]] = each["total_halls"]

    booked_halls_type = {}
    for i in booked_halls_data:
        for key, value in i.items():
            if key == 'category':
                if value in booked_halls_type:
                    booked_halls_type[value] += 1
                else:
                    booked_halls_type[value] = 1

    available_halls = total_halls_inventory
    for key, value in booked_halls_type.items():
        if key in available_halls:
            available_halls[key] -= int(value)

    return available_halls


def delete_booking_service(id):
    booking = BookingHall.objects().get(pk=id)
    booking.delete()
    return jsonify({"message": "Booking Deleted"}), 200


def get_bookings_by_email_service(email):
    bookings = BookingHall.objects().filter(email=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings)), 200
