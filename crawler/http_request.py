# GET/POST/PUT/DELETE/HEAD/OPTIONS

import urllib.request
import urllib.parse

# url="https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0"
# response=urllib.request.urlopen(url)
# data=response.read().decode("utf-8")
# urllib.request.urlretrieve(url,"movie.json")
# print(data)
# print(type(data))


url = "https://login.51job.com/login.php"

# construct post data
data = {"username": "djlove986@126.com","password": "1r4oC0pt"}

# package data
postData = urllib.parse.urlencode(data).encode(encoding="utf-8")

req=urllib.request.Request(url,data=postData)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
)
response=urllib.request.urlopen(req)
print(response.read())