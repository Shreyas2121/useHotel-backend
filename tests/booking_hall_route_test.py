from datetime import datetime
import json
import pytest
from app import app

def test_book_hall():
    data_to_post = {
        "name": "test",
        "email": "test@test.com",
        "date": datetime.now(),
        "checkin": datetime.now(),
        "checkout": datetime.now(),
        "roomType": "Deluxe",
        "roomPrice": 1000,
        "no": 1,
        "selectedAddons": {"Breakfast": 100, "Dinner": 200},
        "couponId": "WELCOME10",
        "discount": "10",
        "specialReq": "None",
        "total": 900
    }
    res = app.test_client().post('/booking/hall', json=data_to_post)

    assert json.loads(res.data)['message'] == "Booking Successful"

def test_check_booking():
    res = app.test_client().post('/booking/hall/check',json={
        "checkIn": str(datetime.now()),
        "checkOut": str(datetime.now())
    })
    assert res.status_code == 200
    assert type(res.json) == dict