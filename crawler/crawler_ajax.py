import urllib.request
import ssl
import json


def ajaxCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    sslcontext = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=sslcontext)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData
    # return jsonStr


# doubanurl = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"
# info = ajaxCrawler(doubanurl)
# print(info)


for i in (1,10):
    url="https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start"+str(i*20)+"&limit=20"
    info=ajaxCrawler(url)
    print(len(info))