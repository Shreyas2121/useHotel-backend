from flask import Flask
from flask_cors import CORS
from routes.halls_route import halls_route
from routes.rooms_route import rooms_route
from routes.coupon_route import coupons_route
from routes.addons_route import addons_route
from routes.booking_room_route import booking_route
from routes.booking_hall_route import booking_hall_route
from routes.reviews_route import reviews_route
from routes.cancelling_room_route import cancel_room_route
from routes.cancelling_hall_route import cancel_hall_route

application = Flask(__name__)
CORS(application)

application.register_blueprint(rooms_route, url_prefix='/api')
application.register_blueprint(halls_route,url_prefix='/api')
application.register_blueprint(coupons_route,url_prefix='/api')
application.register_blueprint(addons_route,url_prefix='/api')
application.register_blueprint(booking_route,url_prefix='/api')
application.register_blueprint(booking_hall_route,url_prefix='/api')
application.register_blueprint(reviews_route,url_prefix='/api')
application.register_blueprint(cancel_room_route,url_prefix='/api')
application.register_blueprint(cancel_hall_route,url_prefix='/api')

if __name__ == '__main__':
    application.run(debug=True)
