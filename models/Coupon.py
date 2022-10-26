from db_connect import connection_db

db = connection_db()

class Coupon(db.Document):
    code = db.StringField(required=True)
    discount_percentage = db.IntField(required=True)

    def to_json(self):
        return {
            "_id": str(self.id),
            "code": self.code,
            "discount_percentage": self.discount_percentage
        }


