array=[48,20,50,40,3,0,56]

for i in range(len(array)-1):
    min_index=i
    for j in range(i,len(array)):
        if array[j]<array[min_index]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]

print(array)
