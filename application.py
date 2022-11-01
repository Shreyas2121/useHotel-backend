from os import environ
from flask import Flask
from flask_cors import CORS
from routes.halls_route import halls_bp
from routes.rooms_route import rooms_bp
from routes.coupon_route import coupons_bp
from routes.addons_route import addons_bp
from routes.booking_room_route import room_booking_bp
from routes.booking_hall_route import hall_booking_bp
from routes.reviews_route import reviews_bp

application = Flask(__name__)

CORS(application)

application.register_blueprint(rooms_bp, url_prefix='/api')
application.register_blueprint(halls_bp, url_prefix='/api')
application.register_blueprint(coupons_bp, url_prefix='/api')
application.register_blueprint(addons_bp, url_prefix='/api')
application.register_blueprint(room_booking_bp, url_prefix='/api')
application.register_blueprint(hall_booking_bp, url_prefix='/api')
application.register_blueprint(reviews_bp, url_prefix='/api')

if __name__ == '__main__':
    application.run(debug=True)
