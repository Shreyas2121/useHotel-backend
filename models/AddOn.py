from db_connect import db_connect

db = db_connect()

class AddOns(db.Document):
    name = db.StringField(required=True)
    price = db.DecimalField(required=True)


    def to_json(self):
        return {
           "_id": str(self.pk),
            "name": self.name,
            "price": self.price
        }

