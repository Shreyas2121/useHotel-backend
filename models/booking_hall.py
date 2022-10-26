import bson
from db_connect import connection_db

db = connection_db()

class BookingHall(db.Document):
    booking_username = db.StringField()
    booking_useremail = db.EmailField()
    booking_date = db.StringField()
    booking_check_in = db.DateTimeField()
    booking_check_out = db.DateTimeField()
    booking_hall_type = db.StringField()
    booking_hall_price = db.DecimalField()
    booking_addOns = db.DictField(field=db.IntField())
    booking_coupon_id = db.StringField(default="")
    booking_coupon_discount = db.StringField(default="")
    booking_total = db.DecimalField()
    booking_special_request = db.StringField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "booking_username": self.booking_username,
            "booking_useremail": self.booking_useremail,
            "booking_date": self.booking_date,
            "booking_hall_type": self.booking_hall_type,
            "booking_hall_price": self.booking_hall_price,
            "booking_addOns": self.booking_addOns,
            "booking_coupon_id": self.booking_coupon_id,
            "booking_coupon_discount": self.booking_coupon_discount,
            "booking_total": self.booking_total,
            "booking_special_request": self.booking_special_request
        }
