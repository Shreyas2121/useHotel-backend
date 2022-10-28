from typing import Any
from flask import jsonify, request, Response
from models.Review import Review


def get_reviews_service():
    review_data = Review.objects()  # type: ignore
    return jsonify({'Review': review.to_json() for review in review_data }),200


def add_reviews_service():
    data: Any = request.get_json()
    Review(
        name = data['name'],
        email = data['email'],
        review = data['review'],
        rating = data['rating'],
    ).save()

    return Response(status=200, mimetype='application/json', response='{"message":"Review Added"}')

def get_top_reviews_service():
    review_data = Review.objects(rating=5)  # type: ignore
    return jsonify({'Review': [review.to_json() for review in review_data ]}),200
