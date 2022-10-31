import mongoengine as db
from os import environ


def db_connect():
    db_connection_uri = "mongodb+srv://shreyas:shreyas@project.kxd4hqz.mongodb.net/?retryWrites=true&w=majority"
    db.connect(host=db_connection_uri)
    return db
