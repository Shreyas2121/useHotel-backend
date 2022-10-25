from db_connect import connection_db

db = connection_db()

class Coupon(db.Document):
    coupons = db.DictField(field=db.IntField())

    def to_json(self):
        return {
            "coupons": self.coupons
        }


