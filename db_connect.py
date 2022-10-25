import  mongoengine as db

def connection_db():
    db_url = "mongodb+srv://shreyas:shreyas@project.kxd4hqz.mongodb.net/?retryWrites=true&w=majority"
    db.connect(host=db_url)
    return db
