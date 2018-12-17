array=[48,20,50,40,3,0,56]

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]
print(array)