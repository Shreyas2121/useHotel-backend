from db_connect import db_connect

db = db_connect()


class Hall(db.Document):
    category = db.StringField(required=True)
    price = db.DecimalField(required=True)
    max_guests = db.IntField(required=True)
    desc = db.StringField(required=True)
    amenities = db.ListField(db.StringField())
    images = db.ListField(db.StringField(), required=True)
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
