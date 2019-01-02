import requests
from xml.etree import ElementTree as ET
r=requests.get("http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=K214&UserID=")
result=r.text
root=ET.XML(result)
for node in root.iter('TrainDetailInfo'):
    print(node.find('TrainStation').text,node.find('ArriveTime').text,node.find("StartTime").text)