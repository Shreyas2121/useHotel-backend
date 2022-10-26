from db_connect import connection_db
from models.coupon import Coupon

db = connection_db()

class BookingRoom(db.Document):
    name = db.StringField()
    email = db.EmailField()
    date = db.DateTimeField()
    check_in_date  = db.DateField()
    check_out_date = db.DateField()
    room_type = db.StringField()
    room_price = db.DecimalField()
    num_of_rooms = db.IntField(default=1)
    add_ons = db.DictField(field=db.IntField())
    coupon = db.DictField()
    total = db.DecimalField()
    special_request = db.StringField()


    def to_json(self):
        return {
            "_id":str(self.pk),
            "name": self.name,
            "email": self.email,
            "date": self.date,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
            "room_type": self.room_type,
            "room_price": self.room_price,
            "num_of_rooms": self.num_of_rooms,
            "add_ons": self.add_ons,
            "coupon": self.coupon,
            "total": self.total,
            "special_request": self.special_request
        }

