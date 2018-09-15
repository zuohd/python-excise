# for i in [1,2,3,4,5]:
#     print(i)
#
# for i in (1,2,3,4,5):
#     print(i)


'''
range([start,]end[,step]) function
'''
# print(range(10))

for x in range(10):
    print(x)

for y in range(2,20,2):
    print(y)


for index,m in enumerate([1,2,3,4,5]): #loop index and element
    print(index,m)

sum=0
for n in range(1,101):
    sum+=n
print(sum)