from db_connect import connection_db

db = connection_db()

class Reviews(db.Document):
    name=db.StringField()
    email = db.StringField()
    reviews = db.StringField()
    rating = db.IntField()

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "reviews": self.reviews,
            "rating": self.rating,
        }