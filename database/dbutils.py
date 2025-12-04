import json
from pymongo import MongoClient
import os

def read_config(path: str = os.path.join(os.getcwd(),"database","config.json")):
    with open(path,'r') as f:
        data = json.load(f)
    return data

CONFIG_DICT = read_config()
MONGO_URI = CONFIG_DICT.get("MONGO_URI", "mongodb://localhost:27017/")


def connect_db(database_name:str,MONGO_URI:str=MONGO_URI):
    DB = MongoClient(MONGO_URI)

    return DB[database_name]

def save_to_database(collection,object):
    collection.insert_one(object)
    print("Saved Sucessfully!!")

def query_database(collection,query:dict[str,str],num_results:int):
    results = collection.find(query).limit(num_results)
    return list(results)