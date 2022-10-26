from db_connect import connection_db

db = connection_db()

class Hall(db.Document):
    hall_id = db.IntField()
    hall_type = db.StringField(requird=True)
    hall_price = db.DecimalField(requird=True)
    hall_max_occ = db.IntField(requird=True)
    hall_desc = db.StringField(requird=True)
    hall_amenities = db.ListField(db.StringField())
    hall_image = db.ListField(db.StringField(),requird=True)
    total_halls = db.IntField(requird=True)


    def to_json(self):
        return {
            "hall_id": self.hall_id,
            "hall_type": self.hall_type,
            "hall_price": self.hall_price,
            "hall_max_occ": self.hall_max_occ,
            "hall_desc": self.hall_desc,
            "hall_image": self.hall_image,
            "total_halls": self.total_halls,
            "hall_amenties": self.hall_amenities
        }
