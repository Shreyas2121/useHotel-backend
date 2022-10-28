from db_connect import db_connect

db = db_connect()


class BookingRoom(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True)
    date = db.DateTimeField(required=True)
    check_in_date = db.DateField(required=True)
    check_out_date = db.DateField(required=True)
    category = db.StringField(required=True)
    price = db.DecimalField(required=True)
    num_of_rooms = db.IntField(default=1)
    add_ons = db.DictField()
    coupon = db.DictField()
    total = db.DecimalField(required=True)
    special_request = db.StringField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "name": self.name,
            "email": self.email,
            "date": self.date,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
            "category": self.category,
            "price": self.price,
            "num_of_rooms": self.num_of_rooms,
            "add_ons": self.add_ons,
            "coupon": self.coupon,
            "total": self.total,
            "special_request": self.special_request
        }
