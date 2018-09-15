'''
filter(fn,lsd)
fn:function parameter
lsd:sequence elements
return all elements macheded ture by function
'''

def func(num):
    if num%2==0:  #odd number
        return True
    return False

list1=[1,2,3,4,5,6,7]
result=filter(func,list1)
print(list(result))
print(list1) #original list not change