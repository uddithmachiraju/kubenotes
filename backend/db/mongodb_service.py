from pymongo import MongoClient

class MongoDBService:
    def __init__(self, uri: str = "mongodb://admin_sanjay:password@localhost:27017/kubenotes_db?authSource=admin", db_name: str = "kubenotes_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def close(self):
        self.client.close() 

    def upload_content(self, content, collection_name: str = "notes"):
        collection = self.get_collection(collection_name) 
        result = collection.insert_one(content)
        inserted_id = result.inserted_id

        # Optional: add the ID into the document if you want it returned with content
        content["_id"] = str(inserted_id)
        return inserted_id 