import json
import pytest
from application import application

def test_get_booking_email_pass():
    response = application.test_client().get('/booking/get/test2@test.com')
    res = json.loads(response.data.decode('utf-8'))[0].get('email')
    assert res == 'test2@test.com'
    assert response.status_code == 200

def test_get_booking_email_fail():
    response = application.test_client().get('/booking/get/ayaan@test.com')
    res = json.loads(response.data.decode('utf-8'))
    assert res == []
    assert response.status_code == 200


def test_cancel_booking_pass():
    response = application.test_client().get('/booking/get/test@gmail.com')
    res = json.loads(response.data.decode('utf-8'))[0].get('_id')
    response_id = app.test_client().delete('/booking/'+str(res))
    res_id = json.loads(response_id.data.decode('utf-8')).get('_id')
    assert res_id == res
    assert response_id.status_code == 200

def test_cancel_booking_fail():
    response = application.test_client().delete('/booking/60a1b1b1b1b1b1b1b1b1b1b1')
    # res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 500
