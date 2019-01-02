import requests
from xml.etree import ElementTree as ET
r=requests.get("http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=345141067")
result=r.text
node=ET.XML(result)
if node.text=="Y":
    print("在线")
else:
    print("离线")