from db_connect import connection_db

db = connection_db()

class Room(db.Document):
    category = db.StringField(requird=True)
    price = db.DecimalField(requird=True)
    occupancy = db.IntField(requird=True)
    desc = db.StringField(requird=True)
    amenities = db.ListField(db.StringField())
    images = db.DictField(field=db.StringField())
    total_rooms = db.IntField(requird=True)
    area_sq_ft = db.FloatField(requird=True)


    def to_json(self):
        return {
            "id": str(self.pk),
            "category": self.category,
            "price": self.price,
            "occupancy": self.occupancy,
            "desc": self.desc,
            "images": self.images,
            "total_rooms": self.total_rooms,
            "amenities": self.amenities,
            "area_sq_ft": self.area_sq_ft
        }

