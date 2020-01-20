import pymongo
from bson.json_util import dumps

class Database:
    def __init__(self, srv, database_name, collection_name):
            self.client = pymongo.MongoClient(srv)
            self.database = self.client.get_database(name=database_name)
            self.collection = self.database.get_collection(name=collection_name)

    def get_all_champs(self):
        for champ in self.collection.find({}):
            return dumps(champ['champion_name'])

    def get_one_champ(self, champ_name):
        for champ in self.collection.find({}):
            if champ['champion_name'] == champ_name:
                return dumps(champ['damage_type'])
                    

    

        
        
    

