def counter(index,n1,n2):
    if index==10:
        return n1
    print("counter:",n1)
    n3=n1+n2
    return counter(index+1,n2,n3)

result=counter(1,0,1)
print("result {index} is {r}".format(index=10,r=result))