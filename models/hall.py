from db_connect import connection_db

db = connection_db()

class Hall(db.Document):
    category = db.StringField(requird=True)
    price = db.DecimalField(requird=True)
    max_guests = db.IntField(requird=True)
    desc = db.StringField(requird=True)
    amenities = db.ListField(db.StringField())
    images = db.ListField(db.StringField(),requird=True)
    total_halls = db.IntField(default=1)


    def to_json(self):
        return {
            "id": str(self.pk),
            "category": self.category,
            "price": self.price,
            "max_guests": self.max_guests,
            "desc": self.desc,
            "images": self.images,
            "total_halls": self.total_halls,
            "amenities": self.amenities
        }
