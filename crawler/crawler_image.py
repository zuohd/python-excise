import urllib.request
import re
import os

def imageCrawler(url,toPath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    response=urllib.request.urlopen(req)
    htmlStr=response.read().decode("utf-8")
    print(htmlStr)
    # with open(r"yhd.html","wb") as f:
    #     f.write(htmlStr)
    patten=r'<div style="position: relative">\n<img src="//(.*?)"/>'
    re_img=re.compile(patten,re.S)
    imglist=re_img.findall(htmlStr)
    print(imglist)
    # print(len(imglist))
    num=1
    for imageUrl in imglist:
        path=os.path.join(toPath,str(num)+".jpg")
        num+=1
        urllib.request.urlretrieve("http://"+imageUrl,filename=path)
url="http://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E8%25A3%2585/"
toPath="images/"
imageCrawler(url,toPath)
