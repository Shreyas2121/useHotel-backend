import pytest
from application import application


def test_check_coupon():
    res = application.test_client().post(
        '/api/coupon/validate', json={'coupon': 'WELCOME10'})
    assert res.status_code == 200


def test_check_coupon_invalid():
    res = application.test_client().post(
        '/api/coupon/validate', json={'coupon': 'WELCOME11'})
    response = res.get_json()
    assert response['message'] == 'Invalid Coupon'


def test_get_coupons():
    res = application.test_client().get('/api/coupons')
    assert res.status_code == 200
