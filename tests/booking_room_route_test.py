from datetime import datetime
import json
import pytest
from application import application


def test_get_booking():
    res = application.test_client().get('/api/booking/room')
    response = json.loads(res.data.decode('utf-8'))
    print(response)
    assert response[0]['name'] == 'test'


def test_book_room():
    data_to_post = {
        "name": "test1",
        "email": "tes2t@test.com",
        "date": datetime.now(),
        "checkin": datetime.now(),
        "checkout": datetime.now(),
        "category": "Deluxe",
        "basePrice": 2000,
        "no": 1,
        "selectedAddons": {"Breakfast": 100, "Dinner": 200},
        "coupon": {
            "code": "test",
        },
        "specialReq": "None",
        "total": 1000
    }
    res = application.test_client().post('api/booking/room', json=data_to_post)

    print(res.data)
    assert json.loads(res.data)['message'] == "Booking Successful"


def test_check_booking():
    res = application.test_client().post('api/booking/room/availability', json={
        "checkIn": str(datetime.now()),
        "checkOut": str(datetime.now())
    })
    assert res.status_code == 200
    assert type(res.json) == dict
