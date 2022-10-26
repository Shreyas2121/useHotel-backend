from typing import Any
from flask import jsonify, request
from models.Review import Review


def service_get_reviews():
    review_data = Reviews.objects()  # type: ignore
    return jsonify({'Reviews': [review.to_json() for review in review_data ]})


def service_add_reviews():
    data: Any = request.get_json()
    Review(
        name = data['name'],
        email = data['email'],
        reviews = data['reviews'],
        rating = data['rating'],
    ).save()
    return jsonify({"message":"Review Added"})

def service_get_top_reviews():
    review_data = Review.objects(rating__gte=5)  # type: ignore
    return jsonify({'Review': [review.to_json() for review in review_data ]})
