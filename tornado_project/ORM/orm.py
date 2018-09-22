from .mysqlclass import MysqlConnect


class ORM(object):

    def save(self):
        tableName = (self.__class__.__name__).lower()
        fieldsStr = valuesStr = "("
        for field in self.__dict__:
            fieldsStr += "%s," % field
            if isinstance(self.__dict__[field], str):
                valuesStr += "'%s'," % self.__dict__[field]
            else:
                valuesStr += "%s," % (str(self.__dict__[field]))
        fieldsStr = "%s)" % (fieldsStr[:len(fieldsStr) - 1])
        valuesStr = "%s)" % (valuesStr[:len(valuesStr) - 1])
        sql = "insert into %s%s values%s" % (tableName, fieldsStr, valuesStr)
        print(sql)
        db = MysqlConnect()
        db.execute_sql(sql)

    @classmethod
    def delete(cls):
        pass

    @classmethod
    def update(cls):
        pass

    @classmethod
    def all(cls):
        table_name=(cls.__name__).lower()
        sql="select * from %s"%table_name
        db=MysqlConnect()
        print(sql)
        return db.get_all_object(sql)

    @classmethod
    def filter(cls):
        pass
