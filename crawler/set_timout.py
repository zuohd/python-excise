import urllib.request

for i in range(1,100):
    try:
        response=urllib.request.urlopen("http://www.baidu.com",timeout=0.5)
        print(len(response.read().decode("utf-8")))

    except:
        print("timeout,next craw")