from db_connect import db_connect

db = db_connect()

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
