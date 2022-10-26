from db_connect import connection_db

db = connection_db()

class Review(db.Document):
    name=db.StringField()
    email = db.EmailField()
    review = db.StringField()
    rating = db.IntField()

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "review": self.review,
            "rating": self.rating,
        }
