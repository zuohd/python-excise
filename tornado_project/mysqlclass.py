import pymysql


class MysqlConnect:
    def __init__(self, host, user, pwd, dbName):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbName = dbName

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
        result=None
        try:
            self.connect()
            cusor = self.db.cursor(pymysql.cursors.DictCursor)
            cusor.execute(sql)
            result=cusor.fetchall()
        except:
            print("Query failed.")
        return result

    def executeSql(self, sql):
        try:
            self.connect()
            affectedCount = self.cursor.execute(sql)
            self.db.commit()
        except:
            print("Execute sql failed.")
            self.db.rollback()
        finally:
            self.cursor.close()
            self.db.close()
        return affectedCount
