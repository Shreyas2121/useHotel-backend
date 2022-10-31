from datetime import datetime
import json
import pytest
from application import  *

def test_book_hall():
    data_to_post = {
        "name": "test",
        "email": "test@test.com",
        "date": datetime.now(),
        "check_in_date": datetime.now(),
        "check_out_date": datetime.now(),
        "category": "Deluxe",
        "price": 1000,
        "no": 1,
        "selectedAddons": {"Breakfast": 100, "Dinner": 200},
        "couponId": "WELCOME10",
        "discount": "10",
        "specialReq": "None",
        "total": 900
    }
    res = .test_client().post('/booking/hall', json=data_to_post)

    assert json.loads(res.data)['message'] == "Booking Successful"

def test_check_booking():
    res = .test_client().post('/booking/hall/check',json={
        "checkIn": str(datetime.now()),
        "checkOut": str(datetime.now())
    })
    assert res.status_code == 200
    assert type(res.json) == dict