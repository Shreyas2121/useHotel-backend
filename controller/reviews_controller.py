from services import reviews_service

def get_reviews_controller():
    return reviews_service.get_reviews_service()

def add_review_controller():
    return reviews_service.add_reviews_service()

def get_top_reviews_controller():
    return reviews_service.get_top_reviews_service()
