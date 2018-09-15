ages=[18,19,20,21,22]
import  math
print(sum(ages)/5)
list1=[]
print(list1)

list2=[1,2,"soderberg",True]
# list2[1]=5
list3=[4,5,6]
list4=list2+list3
print(list4)

list5=[1,2,3,5,8,9]
print(list5*3)
print(list5.index(3))
print(3 in list5)
print(6 in list5)
print(list5[2:6])
print(list5[2:])
print(list5[:6])

two_w_list=[[1,2,3],[4,5,6],[7,8,9]]
print(two_w_list[0][1])

list6=[1,2,3,4,5]
list6.append(6)
# list6.append([7,8,9])
list6.extend([7,8,9])
list6.insert(2,100) #At specific index to insert element,not overwrite
list6.insert(2,[12,13])
list6.pop(2)
print(list6.pop(1))
# print(list6[-1])


list7=[1,2,3]
list7.remove(2) #delete the element content
list7.clear()
print(list7)

list8=[1,3,4,5,8]
# print("abc".find("b",0,2))
index8=list8.index(8)
print(index8)
index9=list8.index(5,2,4)
print(index9)
print(list8.count(4))
print(len(list8))
print(max(list8))
print(min(list8))

list8.reverse()
print(list8)


list9=[34,2,56,4,2,1]
list9.sort()
print(list9)


list10=list9.copy()
list10[1]=0

print(id(list9))
print(id(list10))

a=(1,2,3,4,5) #yuanzu
print(list(a))