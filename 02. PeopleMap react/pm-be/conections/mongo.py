from pymongo import MongoClient
from bson import ObjectId

class Mongo():

    def __init__(self, url):
        self.client = MongoClient(url)
        self.dataBase = self.client['PeopleMap']
        self.keys = ['_id']

    def getOne(self, db:str, filters:dict):
        collection = self.dataBase[db]
        results = self.ConvertObjects(dictionary= collection.find_one(filters))

        return results
    
    def getDataBase(self, db:str, filters:dict = {}, keys:dict = {}, islist:bool = True, count:bool = False):
        collection = self.dataBase[db]

        if count:
            results = collection.count_documents(filters)
        else:
            results = collection.find(filters, keys)

        if islist:
            resultsList:list = [i for i in results]
            return resultsList
            
        return self.ConvertObjects(dictionaryList= results)
    
    def setOne(self, db:str, data:dict):
        collection = self.dataBase[db]
        response = collection.insert_one(data)
        return str(response.inserted_id)

    def ConvertObjects(self, dictionaryList:list = [], dictionary:dict = {}):
        if dictionaryList != [] and dictionaryList != None:
            for i in dictionaryList:
                for k in i.keys():
                    if type(dictionary[k]) == ObjectId:
                        dictionary[k] = str(dictionary[k])
            return dictionaryList

        if dictionary != {} and dictionary != None:
            for i in dictionary.keys():
                if type(dictionary[i]) == ObjectId:
                    dictionary[i] = str(dictionary[i])
        
            return dictionary