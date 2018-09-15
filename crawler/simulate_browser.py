import urllib.request

url = "http://www.baidu.com"

#make request headers
headers = {
    "User-Agent": r"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

req=urllib.request.Request(url,headers=headers)

response=urllib.request.urlopen(req)

data=response.read().decode("utf-8")
print(data)

agentList=[
    "User-Agent: Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
]
import  random
agentStr=random.choice(agentList)
req=urllib.request.Request(url)
req.add_header("User-Agent",agentStr)

response=urllib.request.urlopen(req)

print(response.read().decode("utf-8"))