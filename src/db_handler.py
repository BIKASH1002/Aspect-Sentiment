import pandas as pd
from pymongo import MongoClient
from config.config import MONGO_URI, DB_NAME, COLLECTION_NAME

def connect_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

def insert_data(data):
    collection = connect_db()
    data_dict = data.to_dict("records")
    collection.insert_many(data_dict)
    print("Data inserted to MongoDB!")

def fetch_all_data():
    collection = connect_db()
    return pd.DataFrame(list(collection.find()))
