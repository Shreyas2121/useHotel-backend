from db_connect import connection_db

db = connection_db()

class Room(db.Document):
    room_id = db.IntField()
    room_type = db.StringField(requird=True)
    room_price = db.DecimalField(requird=True)
    room_max_occ = db.IntField(requird=True)
    room_desc = db.StringField(requird=True)
    room_amenities = db.ListField(db.StringField())
    room_images = db.DictField(field=db.StringField())
    room_discount = db.IntField(default=0)
    total_rooms = db.IntField(requird=True)
    room_area = db.StringField(requird=True)


    def to_json(self):
        return {
            "room_id": self.room_id,
            "room_type": self.room_type,
            "room_price": self.room_price,
            "room_max_occ": self.room_max_occ,
            "room_desc": self.room_desc,
            "room_images": self.room_images,
            "total_rooms": self.total_rooms,
            "room_amenties": self.room_amenities,
            "room_area": self.room_area
        }

