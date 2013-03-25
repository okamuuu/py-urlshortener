import pymongo

conn = pymongo.Connection()
db = conn.urlshortener

def find(query):
    return db.urls.find(query)

def find_one(query):
    return db.urls.find_one(query)

def find_and_modify(query, update):
    return db.urls.find_and_modify(query=query, update=update, upsert=True, new=True)

