from functools import reduce

# map(fn,lsd)
# fn:function
# lsd:sequence

def chrToInt(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]


list1 = ["2", "1", "6", "5"]
result = map(chrToInt, list1)
print(list(result))
# for item in result:
#     print(item)

l = map(str, [1, 2, 3, 4])
print(list(l))


#reduce(fn,lsd)
#fn need to accept two parameters,reduce result continue calculate
#reduce(f,[a,b,c,d]) means f(f(f(a,b),c),d)

def mySum(a,b):
    return a+b
list2=[1,2,3,4,5]

sum=reduce(mySum,list2)
print(sum)

#define a map
def myMap(func,li):
    resList=[]
    for parse in li:
        res=func(parse)
        resList.append(res)
    return  resList

print(myMap(chrToInt, list1))