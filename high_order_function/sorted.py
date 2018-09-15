'''
sorted
'''

list1=[4,7,2,6,3]
list2=sorted(list1) #ASC default

print(list2)

list3=[4,-7,-2,6,3]
list4=sorted(list3,key=abs) #key is a function which is customed
list5=sorted(map(abs,list3))
print(list4)
print(list5)



#desc
list6=[4,7,2,6,3]
list7=sorted(list6,reverse=True)
print(list7)

def myLen(str):
    return len(str)

list8=['a','cddd','bbb','eeeee','f1212']
list9=sorted(list8,key=myLen) #key is a function which is customed,or it's built in function (len etc.)
print(list9)