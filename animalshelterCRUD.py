from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    #def __init__(self):
    def __init__(self,username,password):
 
        # Initializing the MongoClient without Authentication
        #self.client = MongoClient('mongodb://localhost:53948')
        # Initializing the MongoClient with Authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:53948/?authMechanism=DEFAULT&authSource=AAC' % (username, password))

        self.database = self.client['AAC']
        
        print("Done")

# Method to implement the C in CRUD - Create.
    def create(self, data):
        if data is not None:
            #insert_dictionary = self.database.animals.insert_one(data)
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Method to implement the R in CRUD - Read.
    def read(self, searchData):
        if searchData is not None:
            # Returns a dictionary from the search
            return self.database.animals.find(searchData,{"_id":False})
        else:
            return False
        
    def readAll(self, searchData):
        data = self.database.animals.find(searchData,{"_id":False})
        return data.raw_result   
    
# Method to implement the U in CRUD - Update.
    def update(self, searchData, newData):
        if searchData is not None:
            data = self.database.animals.update_one(searchData, {'$set': newData})
        else:
            raise Exception("Nothing to update, because data parameter is empty")
        return data.raw_result


# Method to implement the D in CRUD - Delete.
    def delete(self, deleteData):
        if deleteData is not None:
            data = self.database.animals.delete_many(deleteData)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
        return data.raw_result
