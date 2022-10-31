import json
import pytest
from application import application


def test_get_reviews():
    res = application.test_client().get('/api/reviews')
    assert res.status_code == 200


def test_add_reviews():
    data_to_post = {
        "name": "test",
        "email": "test@test.com",
        "review": "test",
        "rating": 5
    }
    res = application.test_client().post('/api/reviews', json=data_to_post)
    print(res.data)
    assert res.status_code == 200
    assert json.loads(res.data) == {"message": "Review Added"}
    assert res.mimetype == 'application/json'
    # assert json.loads(res.data)['message'] == "Review Added"


def test_get_top_reviews():
    res = application.test_client().get('/reviews/featured')
    assert res.status_code == 200
