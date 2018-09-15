# json: {} -dict []-list  :-key value ,-seperator

import json

jsonStr = '{"name":"Jack","age":19,"hobby":["money","power"],"paramters":{"a":1,"b":2}}'

jsondata = json.loads(jsonStr)
print(jsondata)
print(type(jsondata))

print(jsondata["hobby"])

# python data object to json

json2 = {"name": "Jack", "age": 19, "hobby": ["money", "power"], "paramters": {"a": 1, "b": 2}}

jsonStr2 = json.dumps(json2)
print(jsonStr2)
print(type(jsonStr2))

# read local json file

path1 = r"movie.json"

with open(path1,"rb") as f:
    data=json.load(f)
    print(data)
    print(type(data))

#write json to file
path2=r"output.json"

with open(path2,"w") as f:
    json.dump(json2,f)
