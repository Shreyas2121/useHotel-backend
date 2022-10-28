from db_connect import db_connect

db = db_connect()

class BookingHall(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True)
    date = db.DateTimeField(required=True)
    check_in_date = db.DateTimeField(required=True)
    check_out_date = db.DateTimeField(required=True)
    category = db.StringField(required=True)
    price = db.DecimalField(required=True)
    add_ons = db.DictField(field=db.IntField())
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
            "add_ons": self.add_ons,
            "coupon": self.coupon,
            "total": self.total,
            "special_request": self.special_request
        }
