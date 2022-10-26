from db_connect import connection_db

db = connection_db()

class AddOns(db.Document):
    name = db.StringField(required=True)
    price = db.DecimalField(required=True)


    def to_json(self):
        return {
           "_id": str(self.pk),
            "name": self.name,
            "price": self.price
        }

