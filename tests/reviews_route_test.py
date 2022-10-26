import json
import pytest
from app import app


def test_get_reviews():
    res=app.test_client().get('/reviews/')
    assert res.status_code == 200

def test_add_reviews():
    data_to_post={
        "name": "test",
        "email": "test@test.com",
        "reviews": "test",
        "rating": 5
    }
    res=app.test_client().post('/reviews/',json=data_to_post)
    print(res.data)
    assert json.loads(res.data)['message'] == "Review Added"

def test_get_top_reviews():
    res=app.test_client().get('/reviews/featured')
    assert res.status_code == 200




