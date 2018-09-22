import pymysql
import config


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class MysqlConnect:

    def __init__(self):
        self.host = config.mysql.get("host")
        self.user = config.mysql.get("user")
        self.pwd = config.mysql.get("password")
        self.dbName = config.mysql.get("dbName")

    def connect(self):
        self.db = pymysql.connect(self.host, self.user, self.pwd, self.dbName)
        self.cusor = self.db.cursor()

    def close(self):
        self.cusor.close()
        self.db.close()

    def getOne(self, sql):
        result = None
        try:
            self.connect()
            self.cusor.execute(sql)
            result = self.cusor.fetchone()
        except:
            print("Query failed.")
        return result

    def getAll(self, sql):
        result = None
        try:
            self.connect()
            self.cusor.execute(sql)
            result = self.cusor.fetchall()
        except:
            print("Query failed.")
        return result

    def get_all_object(self, sql):
        result = None
        try:
            self.connect()
            cusor = self.db.cursor(pymysql.cursors.DictCursor)
            cusor.execute(sql)
            result = cusor.fetchall()
        except:
            print("Query failed.")
        return result

    def execute_sql(self, sql):
        affectedCount=0
        self.connect()
        try:
            affectedCount = self.cusor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("Execute sql failed.",e)
            self.db.rollback()
        finally:
            self.close()
        return affectedCount
