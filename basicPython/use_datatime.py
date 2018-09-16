import datetime

'''
firstly import datetime module,
which included classes:
datetime,timedelta,tzinfo,time,date
'''
d1=datetime.datetime.now()
print(d1)
print(type(d1))


d2=datetime.datetime(1999,10,1,10,34,12,123456)
print(d2)


#convert datetime to string
d3=d1.strftime("%Y-%m-%d %X")
print(d3)
print(type(d3))


d4=datetime.datetime.strptime(d3,"%Y-%m-%d %X")
print(d4)


d5=datetime.datetime(1999,10,1,10,34,12,123456)
d6=datetime.datetime.now()
d7=d6-d5
print(d7)
print(type(d7))
print(d7.days)
print(d7.seconds) #which not include days
print(d7.total_seconds())
