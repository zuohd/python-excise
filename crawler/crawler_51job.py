import urllib.request
import ssl
import json

def jobsCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    sslcontext = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=sslcontext)
    HTML = response.read().decode("utf-8")



url="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
info=jobsCrawler(url)
print(info)