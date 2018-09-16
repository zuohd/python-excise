import pymysql


db=pymysql.connect("localhost","root","root123","study")

cursor=db.cursor()

# sql="select * from student"
#
# cursor.execute(sql)
# data=cursor.fetchone()///fetchall/rowcount
#
# print(data)
# print(type(data))
# cursor.close()
# db.close()

sql="insert into class values(0,'aaa')"

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
finally:
    cursor.close()
    db.close()