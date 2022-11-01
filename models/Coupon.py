from db_connect import db_connect

db = db_connect()


class Coupon(db.Document):
    code = db.StringField(required=True)
    discount_percentage = db.IntField(required=True)

    def to_json(self):
        return {
            "_id": str(self.pk),
            "code": self.code,
            "discount_percentage": self.discount_percentage
        }
