from db_connect import connection_db

db = connection_db()

class Hall(db.Document):
    type = db.StringField(requird=True)
    price = db.DecimalField(requird=True)
    max_guests = db.IntField(requird=True)
    desc = db.StringField(requird=True)
    amenities = db.ListField(db.StringField())
    images = db.ListField(db.StringField(),requird=True)
    total_halls = db.IntField(requird=True)


    def to_json(self):
        return {
            "id": str(self.pk),
            "type": self.type,
            "price": self.price,
            "max_guests": self.max_guests,
            "desc": self.desc,
            "images": self.images,
            "total_halls": self.total_halls,
            "amenties": self.amenities
        }
