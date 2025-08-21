import pymongo
from pymongo.errors import DuplicateKeyError, BulkWriteError
import logging

log = logging.getLogger(__name__)

class MongoDBClient:

    def __init__(self, database):
        database_name = MongoDBClient.databases[database]
        self.database = MongoDBClient.mongo_client[database_name]

    @classmethod
    def set_client(cls, context):
        MongoDBClient.mongo_client = pymongo.MongoClient(f"mongodb://{context.config.get('MONGO_URL')}:{context.config.get('MONGO_PORT')}/", heartbeatFrequencyMS=context.config.get('MONGO_HEARTBEAT_MS'))
        MongoDBClient.databases = context.config.get('MONGO_DBS')

    def insert_one(self, data_dict, collection_name):
        collection = self.database[collection_name]

        try: 
            action = collection.insert_one(data_dict)
            return_json = {'action': 'Insert', 'json': data_dict}
            
        except DuplicateKeyError:
            print ("duplicated key, solve me please")
        return return_json
    
    def insert_many(self, data_list, collection_name):
        collection = self.database[collection_name]

        log.debug(f"Inserting: {data_list}")
        log.debug(f"Colection: {collection_name}")

        try: 
            action = collection.insert_many(data_list, ordered=False)
            log.debug(f"Result: {action}")
            
            
        except BulkWriteError as bwe:
            for error in bwe.details['writeErrors']:
                if error['code'] == 11000: # 11000 is the duplicate key error code
                    print(f"Duplicate key error for document: {error['op']}")

        return_json = {'action': 'Insert', 'json': data_list}
        return return_json
    
    def index_unique_validation(self, collection_name, index_name):
        collection = self.database[collection_name]
        indexes = collection.index_information()

        if not index_name in indexes:
            collection.create_index(index_name, unique=1)

    def get_current_client():
        return MongoDBClient.mongo_client