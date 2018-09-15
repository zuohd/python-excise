import  urllib.request
import ssl
import re

def jokeCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    sslcontext = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=sslcontext)
    HTML=response.read().decode("utf-8")
    pat=r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'

    re_joke=re.compile(pat,re.S)
    divlist=re_joke.findall(HTML)
    # print(divlist)
    # print(len(divlist))
    # with open("qiushi.html","w") as f:
    #     f.write(HTML)

    dic={}
    for div in divlist:
        re_u=re.compile(r"<h2>(.*?)</h2>",re.S)
        username=re_u.findall(div)
        user1=username[0]
        re_d=re.compile(r'<div class="content">\n<span>\n(.*?)</span>',re.S)
        joke=re_d.findall(div)

        dic[user1]=joke[0]
    return dic

url="https://www.qiushibaike.com/8hr/page/1/"
info=jokeCrawler(url)
for k,v in info.items():
    print(k,v)