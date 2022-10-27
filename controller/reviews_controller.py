from services import reviews_service

def get_reviews_controller():
    return reviews_service.service_get_reviews()

def add_review_controller():
    return reviews_service.service_add_reviews()

def get_top_reviews_controller():
    return reviews_service.service_get_top_reviews()



