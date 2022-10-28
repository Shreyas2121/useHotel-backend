import mongoengine as db
from os import environ


def db_connect():
    db_connection_uri = environ.get('FLASK_DB_URL')
    db.connect(host=db_connection_uri)
    return db
