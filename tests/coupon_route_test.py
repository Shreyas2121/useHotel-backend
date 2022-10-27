import pytest
from app import app

def test_check_coupon():
    res = app.test_client().post('/booking/coupon',json={'coupon':'WELCOME10'})
    assert res.status_code == 200

def test_check_coupon_invalid():
    res = app.test_client().post('/booking/coupon',json={'coupon':'WELCOME11'})
    assert res.data == b'Invalid Coupon'

def test_get_coupons():
    res = app.test_client().get('/booking/coupon/get')
    assert res.status_code == 200
