from mongoengine import connect,disconnect,Document
class MongoEngine:
    __engine = None
    def __init__(self):
        self.engine = connect('MP',host='localhost',port=27017)
        self.__engine = self.engine
    def save(self, data):
        if isinstance(data, Document):
            data.save()
        else:
            raise Exception('Data is not an instance of Document')
    def get_engine(self):
        return self.__engine
    def close_engine(self):
        disconnect()
