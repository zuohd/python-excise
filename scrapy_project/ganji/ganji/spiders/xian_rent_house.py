# -*- coding: utf-8 -*-
import scrapy
from ..items import GanjiItem as RentInformation


class XianRentHouseSpider(scrapy.Spider):
    name = 'zufang'
    allowed_domains = ['xa.ganji.com']
    start_urls = ['http://xa.ganji.com/fang1/lianhu/']

    def parse(self, response):
        title_list=response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd/a/text()").extract()
        money_list=response.xpath("//div[@class='price']/span[1]/text()").extract()
        rentItem = RentInformation()
        for t,m in zip(title_list,money_list):
            rentItem['title']=t
            rentItem['money']=m
            yield rentItem


