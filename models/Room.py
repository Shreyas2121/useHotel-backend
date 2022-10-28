from db_connect import db_connect

db = db_connect()

class Room(db.Document):
    category = db.StringField(required=True)
    price = db.DecimalField(required=True)
    occupancy = db.IntField(required=True)
    desc = db.StringField(required=True)
    amenities = db.ListField(db.StringField())
    images = db.DictField(field=db.StringField())
    total_rooms = db.IntField(required=True)
    area_sq_ft = db.FloatField(required=True)


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

