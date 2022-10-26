from services import reviews_service

def get_reviews():
    return reviews_service.service_get_reviews()

def add_reviews():
    return reviews_service.service_add_reviews()

def get_top_reviews():
    return reviews_service.service_get_top_reviews()



