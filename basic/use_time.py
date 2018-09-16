import time
'''
UTC-chna=utc+8
DST:summer time

time formate:
1.timestamp:from 1970-1-1
2.tuple
3.string formate
'''

c=time.time()
print(c)#return current timestamp
print(type(c))


t=time.gmtime(c) #utc time with timestamp
print(t)
print(type(t))


b=time.localtime(c)
print(b)
print(type(b))

m=time.mktime(b) #convert localtime to timestamp
print(m)


timeStr=time.asctime(b) #convert tuple to time string
print(timeStr)


timeStr1=time.ctime(c)
print(timeStr)
print(type(timeStr1))


timeStr2=time.strftime("%Y-%m-%d %H:%M:%S",b) #if ommit b default current local time
timeStr3=time.strftime("%Y-%m-%d %X") #if ommit b default current local time

print(timeStr2)
print(timeStr3)


timeTuple=time.strptime(timeStr3,"%Y-%m-%d %X")
print(timeTuple)


time.sleep(4) #delay parameter:int or float or decimal

clock=time.clock() #return cpu execute time
print(clock)

time.sleep(50)
clock1=time.clock()
print(clock1)