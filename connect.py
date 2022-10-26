import  mongoengine as db
from application import application
from os import environ

def connection_db():
    db_url = environ.get('FLASK_DB_URL')
    db.connect(host=db_url)
    return db
