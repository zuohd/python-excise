import re
print(re.match("www","www.baidu.com"))
print(re.match("wwW","www.baidu.com"))

print(re.match("www","wwW.baidu.com",flags=re.I).span())

print(re.search("soderberg","good man is soderberg,s xxxx"))
print(re.findall("soder","xxx soder!aaa,soder,soderberg fine"))

# def checkPhone(str):
#     if len(str)!=11:
#         return  False
#     elif str[0]!="1":
#         return False
#     elif str[1:3] not in ["39","36","37","38"]:
#         return  False
#     for i in str:
#         if i<"0" or i>"9":
#             return False
#     return True
#
#
# print(checkPhone("13649284753"))
# print(checkPhone("1364a284753"))
#
# print(checkPhone("236492847533"))
# print(checkPhone("436492b4753"))
