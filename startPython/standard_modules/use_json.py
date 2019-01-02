import json

dict_str = '{"k1":"v1","k2":"v2"}'
print(type(dict_str))
dict_json = json.loads(dict_str)
print(type(dict_json))
json_li = [11, 22, 33, 44]
print(type(json_li))
json_str = json.dumps(json_li)
print(type(json_str))
print(json_str)
