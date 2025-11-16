import json
from pymongo import MongoClient

def read_config(path: str = r"config.json"):
    with open(path,'r') as f:
        data = json.load(f)
    return data

CONFIG_DICT = read_config()
MONGO_URI = CONFIG_DICT.get("MONGO_URI", "mongodb://localhost:27017/")


def connect_db(MONGO_URI:str=MONGO_URI):
    DB = MongoClient(MONGO_URI)

    return DB