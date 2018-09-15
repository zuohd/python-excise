import urllib.request

# urllib.request.urlretrieve("http://www.baidu.com",filename="file2.html")
# urllib.request.urlcleanup()
# send request to specific url and return server response data object
response=urllib.request.urlopen("http://www.baidu.com")

# data=response.read()


# data=response.readline()

data=response.readlines()
print(data)
print(len(data))
print(type(data))
print(data[50].decode("utf-8"))
print(response.info())
print(response.getcode())
print(response.geturl())
#if response.getcode()==200 or response.getcode()=304


url=r"https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%BC%80%E5%AD%A6%E7%AC%AC%E4%B8%80%E8%AF%BE2018&rsv_pq=9fc427650003686a&rsv_t=f3d7UDGDdcqUwAZZ43G5%2FADh3eTdTLTMJ3zfO0kGRUpEHeP9lNSeEPDPWjI&rqlang=cn&rsv_enter=1&rsv_sug3=2&rsv_sug1=3&rsv_sug7=101&rsv_sug2=1&prefixsug=k&rsp=0&inputT=6965&rsv_sug4=8273"
newurl=urllib.request.unquote(url)
# newurl=urllib.request.quote(url)
print(newurl)
# with open("file1.html","wb") as f:
#     f.write(data)