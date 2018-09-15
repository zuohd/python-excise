import pickle #persite data ,including set\list\tuple\dict etc.


# mylist=[1,2,3,4,5,"abc"]
# f1=open("testfile","wb")
# pickle.dump(mylist,f1)
# f1.close()

#read
f2=open("testfile","rb")
templist=pickle.load(f2)
print(templist)
f2.close()
