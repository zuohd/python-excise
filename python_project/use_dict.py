'''
key-value data ,high speed search and high speed inserting,list is slower as growing data
occupy the big memory,list occupy the little memory
Dictionary is unordered
key must be unique;
key must be not changed object.
key can be string/int
list can be changed so it's not as key.
'''

dict1 = {"tom": 60, "lilei": 70}
print(dict1)
print(dict1["lilei"])  # dict1[key]
print(dict1.get("xxxx"))

print(dict1.keys())
print(dict1.values())

dict1["hanmeimei"] = 90  # has will be append else will be modified.
dict1["tom"] = 80  # modify the specific key value
print(dict1)

dict1.pop("tom")
print(dict1)
print(type(dict1))

# loops the dictionary
for key in dict1:
    print(key, dict1[key])

for k, v in dict1.items():
    print(k, v)

for i, v2 in enumerate(dict1):
    print(i, v2)
