from typing import Any
from flask import Response, jsonify, request
from dateutil import parser
from services.rooms_service import get_rooms_service

from models.BookingRoom import BookingRoom


def book_room_service():
    data: Any = request.get_json()
    print(data)
    try:
        obj = BookingRoom(
            name=data['name'],
            email=data['email'],
            date=data['date'],
            check_in_date=data['checkin'],
            check_out_date=data['checkout'],
            category=data['roomType'],
            price=data['roomPrice'],
            num_of_rooms=data['no'],
            add_ons=data['selectedAddons'],
            coupon=data['coupon'],
            special_request=data['specialReq'],
            total=data['total'],
        )
        obj.save()
    except Exception as e:
        return jsonify({'message': 'Error Occured'}), 400

    return jsonify({"message": "Booking Successful"})


def get_room_bookings_service():
    bookings = BookingRoom.objects()
    return Response(status=200, mimetype='application/json', response=list(map(lambda x: x.to_json(), bookings)))


def get_room_availability_service():
    data: Any = request.get_json()
    parsed_check_in = parser.isoparse(data['checkIn'])
    parsed_check_out = parser.isoparse(data['checkOut'])

    if parsed_check_in > parsed_check_out:
        return jsonify({"message": "Check in date should be before check out date"}), 400

    booking_room_checkin = list(map(lambda x: x.to_json(), BookingRoom.objects(check_in_date__lte=parsed_check_in,
                                                                               check_out_date__gt=parsed_check_in, )))
    booking_room_checkout = list(map(lambda x: x.to_json(), BookingRoom.objects(check_in_date__lt=parsed_check_out,
                                                                                check_out_date__gte=parsed_check_out, )))
    booking_room_between = list(map(lambda x: x.to_json(), BookingRoom.objects(check_in_date__gte=parsed_check_in,
                                                                               check_out_date__lte=parsed_check_out, )))

    booking_room_checkout.extend(x for x in booking_room_checkin if x not in booking_room_checkout)
    booking_room_checkout.extend(x for x in booking_room_between if x not in booking_room_checkout)

    rooms = get_rooms_service()
    available_rooms = {}
    for each in rooms[0].json.get('rooms'):
        available_rooms[each["category"]] = each["total_rooms"]

    booked_room_type = {}
    for i in booking_room_checkout:
        for key, value in i.items():
            if key == 'category':
                if value in booked_room_type:
                    booked_room_type[value] = booked_room_type[value] + i['num_of_rooms']
                else:
                    booked_room_type[value] = i['num_of_rooms']

    for key, value in booked_room_type.items():
        if key in available_rooms:
            available_rooms[key] -= int(value)

    return available_rooms


def delete_booking_service(id):
    booking = BookingRoom.objects().get(pk=id)
    print('test')
    print(booking)
    booking.delete()
    return jsonify({"message": "Room Booking Deleted"}), 200


def get_bookings_by_email_service(email):
    bookings = BookingRoom.objects().filter(email=email)
    print(bookings)
    return list(map(lambda x: x.to_json(), bookings)), 200
