import redis


class SoderbergRedis:
    def __init__(self, password, host="localhost", port=6379):
        self.__redis = redis.StrictRedis(host=host, port=port, password=password)

    def setKeyValue(self, key, value):
        self.__redis.set(key, value)

    def getKeyValue(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
