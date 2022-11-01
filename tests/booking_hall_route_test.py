from datetime import datetime
import json
import pytest
from application import application

def test_book_hall():
    data_to_post = {
        "name": "test1",
        "email": "tes2t@test.com",
        "date": datetime.now(),
        "checkin": datetime.now(),
        "checkout": datetime.now(),
        "category": "Deluxe",
        "basePrice": 20000,
        "no": 1,
        "selectedAddons": {"Breakfast": 100, "Dinner": 200},
        "coupon": {
            "code": "test",
        },
        "specialReq": "None",
        "total": 1000
    }
    res = application.test_client().post('api/booking/hall', json=data_to_post)

    assert json.loads(res.data)['message'] == "Booking Successful"

def test_check_booking():
    res = application.test_client().get(f'api/booking/hall/availability?checkIn={str(datetime.now())}&checkOut={str(datetime.now())}')
    assert res.status_code == 200
    assert type(res.json) == dict