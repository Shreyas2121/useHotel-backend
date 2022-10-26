from db_connect import connection_db

db = connection_db()

class AddOns(db.Document):
    addOn_type = db.DictField(field=db.IntField())


    def to_json(self):
        return {
            "addOn_type": self.addOn_type,
        }

